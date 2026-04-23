#!/usr/bin/env python3
"""Local review server for career-related ChatGPT export threads.

The raw ChatGPT export is treated as read-only. Generated indexes and review
labels are kept under 99_private/derived/<topic>/.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import re
import sys
import urllib.parse
from dataclasses import dataclass
from datetime import datetime, timezone
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any


DEFAULT_TOPIC = "career"
DEFAULT_EXPORT_DIR = Path("99_private") / "20260422ChatGPT_Export"
DEFAULT_DERIVED_ROOT = Path("99_private") / "derived"
LABEL_STATUSES = ("unread", "include", "maybe", "exclude")

KEYWORDS = [
    {"term": "転職", "weight": 12, "kind": "decisive"},
    {"term": "職務経歴", "weight": 11, "kind": "decisive"},
    {"term": "履歴書", "weight": 10, "kind": "decisive"},
    {"term": "志望動機", "weight": 10, "kind": "decisive"},
    {"term": "面接", "weight": 9, "kind": "decisive"},
    {"term": "応募", "weight": 9, "kind": "decisive"},
    {"term": "求人", "weight": 8, "kind": "decisive"},
    {"term": "内定", "weight": 8, "kind": "decisive"},
    {"term": "採用", "weight": 7, "kind": "decisive"},
    {"term": "退職", "weight": 7, "kind": "decisive"},
    {"term": "キャリア", "weight": 6, "kind": "decisive"},
    {"term": "前職", "weight": 6, "kind": "context"},
    {"term": "エプソン", "weight": 6, "kind": "context"},
    {"term": "Epson", "weight": 6, "kind": "context"},
    {"term": "休職", "weight": 5, "kind": "context"},
    {"term": "復職", "weight": 4, "kind": "context"},
    {"term": "年収", "weight": 4, "kind": "context"},
    {"term": "コーンズ", "weight": 2, "kind": "noisy"},
    {"term": "Cornes", "weight": 2, "kind": "noisy"},
]


@dataclass(frozen=True)
class Paths:
    repo_root: Path
    export_dir: Path
    derived_dir: Path
    index_path: Path
    csv_path: Path
    labels_path: Path


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Build and serve a local review UI for career-related ChatGPT export threads."
    )
    parser.add_argument(
        "--export-dir",
        default=str(DEFAULT_EXPORT_DIR),
        help="ChatGPT export directory containing conversations-*.json.",
    )
    parser.add_argument("--topic", default=DEFAULT_TOPIC, help="Derived topic directory name.")
    parser.add_argument("--host", default="127.0.0.1", help="Bind host.")
    parser.add_argument("--port", type=int, default=8765, help="Bind port. Use 0 for an available port.")
    parser.add_argument("--rebuild", action="store_true", help="Rebuild the candidate index before serving.")
    parser.add_argument("--build-only", action="store_true", help="Build the candidate index and exit.")
    parser.add_argument(
        "--min-score",
        type=int,
        default=8,
        help="Minimum score for contextual-only candidates.",
    )
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parents[1]
    paths = make_paths(repo_root, Path(args.export_dir), args.topic)

    validate_readonly_export(paths.export_dir)
    ensure_private_output(paths)

    if args.rebuild or not paths.index_path.exists():
        count = build_index(paths, min_score=args.min_score)
        print(f"Built {count} candidates: {paths.index_path}")
    else:
        print(f"Using existing index: {paths.index_path}")

    ensure_labels_file(paths.labels_path)

    if args.build_only:
        return 0

    server = ReviewServer((args.host, args.port), ReviewHandler, paths)
    host, port = server.server_address[:2]
    print(f"Career review server: http://{host}:{port}/")
    print("Press Ctrl+C to stop.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")
    finally:
        server.server_close()
    return 0


def make_paths(repo_root: Path, export_dir_arg: Path, topic: str) -> Paths:
    if export_dir_arg.is_absolute():
        export_dir = export_dir_arg.resolve()
    else:
        export_dir = (repo_root / export_dir_arg).resolve()

    safe_topic = re.sub(r"[^A-Za-z0-9_-]+", "_", topic).strip("_") or DEFAULT_TOPIC
    derived_dir = (repo_root / DEFAULT_DERIVED_ROOT / safe_topic).resolve()
    return Paths(
        repo_root=repo_root,
        export_dir=export_dir,
        derived_dir=derived_dir,
        index_path=derived_dir / f"{safe_topic}_index.jsonl",
        csv_path=derived_dir / f"{safe_topic}_candidates.csv",
        labels_path=derived_dir / f"{safe_topic}_labels.json",
    )


def validate_readonly_export(export_dir: Path) -> None:
    if not export_dir.exists():
        raise SystemExit(f"Export directory does not exist: {export_dir}")
    if not export_dir.is_dir():
        raise SystemExit(f"Export path is not a directory: {export_dir}")
    if not list(export_dir.glob("conversations-*.json")):
        raise SystemExit(f"No conversations-*.json files found in: {export_dir}")


def ensure_private_output(paths: Paths) -> None:
    private_root = (paths.repo_root / "99_private").resolve()
    try:
        paths.derived_dir.relative_to(private_root)
    except ValueError as exc:
        raise SystemExit(f"Refusing to write outside 99_private: {paths.derived_dir}") from exc
    paths.derived_dir.mkdir(parents=True, exist_ok=True)


def ensure_labels_file(path: Path) -> None:
    if path.exists():
        return
    write_json_atomic(path, {"version": 1, "labels": {}})


def build_index(paths: Paths, min_score: int) -> int:
    records: list[dict[str, Any]] = []
    for source_path in sorted(paths.export_dir.glob("conversations-*.json")):
        conversations = read_json(source_path)
        if not isinstance(conversations, list):
            continue
        for source_index, conversation in enumerate(conversations):
            record = candidate_record(conversation, source_path.name, source_index, min_score)
            if record:
                records.append(record)

    records.sort(key=lambda item: (item.get("updated_sort") or 0, item.get("created_sort") or 0), reverse=True)

    with paths.index_path.open("w", encoding="utf-8", newline="\n") as handle:
        for record in records:
            public_record = {key: value for key, value in record.items() if not key.endswith("_sort")}
            handle.write(json.dumps(public_record, ensure_ascii=False, separators=(",", ":")) + "\n")

    write_candidates_csv(paths.csv_path, records)
    return len(records)


def candidate_record(
    conversation: dict[str, Any],
    source_file: str,
    source_index: int,
    min_score: int,
) -> dict[str, Any] | None:
    title = str(conversation.get("title") or "Untitled")
    conversation_id = str(conversation.get("conversation_id") or conversation.get("id") or f"{source_file}:{source_index}")
    nodes = conversation_nodes(conversation)
    current_ids = current_path_ids(conversation, nodes)
    messages = nodes_to_messages(nodes, current_ids)
    searchable_messages = [message for message in messages if message["text"]]
    if not searchable_messages and not title:
        return None

    current_messages = [message for message in searchable_messages if message.get("in_current_path")]
    visible_messages = current_messages if current_messages else searchable_messages

    combined_text = title + "\n" + "\n".join(message["text"] for message in searchable_messages)
    score_data = score_text(combined_text)
    if not is_candidate(score_data, min_score):
        return None

    snippets = make_snippets(searchable_messages, score_data["hit_terms"])
    create_time = as_float(conversation.get("create_time") or conversation.get("created_at"))
    update_time = as_float(conversation.get("update_time") or conversation.get("updated_at"))

    return {
        "id": conversation_id,
        "source_file": source_file,
        "source_index": source_index,
        "title": title,
        "created": iso_from_epoch(create_time),
        "updated": iso_from_epoch(update_time),
        "created_sort": create_time,
        "updated_sort": update_time,
        "message_count": len(visible_messages),
        "all_message_count": len(searchable_messages),
        "score": score_data["score"],
        "decisive_score": score_data["decisive_score"],
        "context_score": score_data["context_score"],
        "hit_terms": score_data["hit_terms"],
        "hit_counts": score_data["hit_counts"],
        "search_text": make_search_text(title, visible_messages),
        "snippets": snippets,
    }


def conversation_nodes(conversation: dict[str, Any]) -> list[dict[str, Any]]:
    mapping = conversation.get("mapping")
    if isinstance(mapping, dict):
        nodes: list[dict[str, Any]] = []
        for node_id, node in mapping.items():
            if isinstance(node, dict):
                nodes.append(
                    {
                        "node_id": str(node_id),
                        "parent": node.get("parent"),
                        "children": node.get("children") or [],
                        "message": node.get("message"),
                    }
                )
        return nodes

    messages = conversation.get("messages")
    if isinstance(messages, list):
        return [
            {"node_id": str(index), "parent": None, "children": [], "message": message}
            for index, message in enumerate(messages)
        ]

    return []


def current_path_ids(conversation: dict[str, Any], nodes: list[dict[str, Any]]) -> set[str]:
    node_by_id = {node["node_id"]: node for node in nodes}
    current = conversation.get("current_node")
    if not current:
        return set(node_by_id)

    path: list[str] = []
    seen: set[str] = set()
    while current and current in node_by_id and current not in seen:
        seen.add(str(current))
        path.append(str(current))
        current = node_by_id[str(current)].get("parent")
    return set(reversed(path))


def nodes_to_messages(nodes: list[dict[str, Any]], current_ids: set[str]) -> list[dict[str, Any]]:
    messages: list[dict[str, Any]] = []
    for index, node in enumerate(nodes):
        raw_message = node.get("message")
        if not isinstance(raw_message, dict):
            continue
        metadata = raw_message.get("metadata")
        hidden = bool(isinstance(metadata, dict) and metadata.get("is_visually_hidden_from_conversation"))
        if hidden:
            continue
        text = content_to_text(raw_message.get("content"))
        if not text.strip():
            continue
        author = raw_message.get("author")
        role = "unknown"
        if isinstance(author, dict):
            role = str(author.get("role") or "unknown")
        created = as_float(raw_message.get("create_time") or raw_message.get("update_time"))
        node_id = str(node.get("node_id") or index)
        messages.append(
            {
                "id": str(raw_message.get("id") or node_id),
                "node_id": node_id,
                "role": role,
                "role_label": role_label(role),
                "created": iso_from_epoch(created),
                "created_sort": created,
                "text": text,
                "in_current_path": node_id in current_ids,
            }
        )

    return sorted(messages, key=lambda message: (message["created_sort"] or 0, message["node_id"]))


def content_to_text(content: Any) -> str:
    if isinstance(content, str):
        return content
    if not isinstance(content, dict):
        return ""
    parts = content.get("parts")
    if isinstance(parts, list):
        texts = [part_to_text(part) for part in parts]
        return "\n\n".join(text for text in texts if text).strip()
    return part_to_text(content).strip()


def part_to_text(part: Any) -> str:
    if isinstance(part, str):
        return part
    if isinstance(part, dict):
        for key in ("text", "name", "url"):
            value = part.get(key)
            if isinstance(value, str) and value.strip():
                return value
        nested = part.get("parts")
        if isinstance(nested, list):
            return "\n\n".join(part_to_text(item) for item in nested if part_to_text(item)).strip()
    return ""


def score_text(text: str) -> dict[str, Any]:
    hit_counts: dict[str, int] = {}
    hit_terms: list[str] = []
    decisive_score = 0
    context_score = 0
    noisy_score = 0

    for keyword in KEYWORDS:
        term = keyword["term"]
        count = count_occurrences(text, term)
        if count == 0:
            continue
        hit_counts[term] = count
        hit_terms.append(term)
        weighted = min(count, 8) * int(keyword["weight"])
        if keyword["kind"] == "decisive":
            decisive_score += weighted
        elif keyword["kind"] == "context":
            context_score += weighted
        else:
            noisy_score += weighted

    score = decisive_score + context_score
    if decisive_score or context_score:
        score += min(noisy_score, 10)

    return {
        "score": score,
        "decisive_score": decisive_score,
        "context_score": context_score,
        "noisy_score": noisy_score,
        "hit_terms": hit_terms,
        "hit_counts": hit_counts,
    }


def count_occurrences(text: str, term: str) -> int:
    if not term:
        return 0
    return len(re.findall(re.escape(term), text, flags=re.IGNORECASE))


def is_candidate(score_data: dict[str, Any], min_score: int) -> bool:
    if score_data["decisive_score"] > 0:
        return True
    return score_data["context_score"] >= min_score


def make_snippets(messages: list[dict[str, Any]], hit_terms: list[str], limit: int = 3) -> list[dict[str, str]]:
    snippets: list[dict[str, str]] = []
    for message in messages:
        text = message["text"]
        for term in hit_terms:
            match = re.search(re.escape(term), text, flags=re.IGNORECASE)
            if not match:
                continue
            start = max(match.start() - 90, 0)
            end = min(match.end() + 150, len(text))
            snippet = text[start:end].replace("\r\n", "\n").replace("\r", "\n")
            snippet = re.sub(r"\s+", " ", snippet).strip()
            if start > 0:
                snippet = "..." + snippet
            if end < len(text):
                snippet = snippet + "..."
            snippets.append(
                {
                    "term": term,
                    "role": str(message.get("role") or ""),
                    "created": str(message.get("created") or ""),
                    "text": snippet,
                }
            )
            break
        if len(snippets) >= limit:
            break
    return snippets


def make_search_text(title: str, messages: list[dict[str, Any]]) -> str:
    parts = [title]
    for message in messages:
        role = str(message.get("role_label") or message.get("role") or "")
        text = str(message.get("text") or "")
        if text:
            parts.append(role)
            parts.append(text)
    return re.sub(r"\s+", " ", "\n".join(parts)).strip()


def write_candidates_csv(path: Path, records: list[dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "id",
                "title",
                "created",
                "updated",
                "score",
                "hit_terms",
                "source_file",
                "source_index",
                "status",
                "notes",
            ],
        )
        writer.writeheader()
        for record in records:
            writer.writerow(
                {
                    "id": record["id"],
                    "title": record["title"],
                    "created": record["created"],
                    "updated": record["updated"],
                    "score": record["score"],
                    "hit_terms": ";".join(record["hit_terms"]),
                    "source_file": record["source_file"],
                    "source_index": record["source_index"],
                    "status": "",
                    "notes": "",
                }
            )


class ReviewServer(ThreadingHTTPServer):
    def __init__(self, server_address: tuple[str, int], handler: type[BaseHTTPRequestHandler], paths: Paths):
        super().__init__(server_address, handler)
        self.paths = paths


class ReviewHandler(BaseHTTPRequestHandler):
    server: ReviewServer

    def do_GET(self) -> None:
        parsed = urllib.parse.urlparse(self.path)
        route = parsed.path
        if route == "/":
            self.send_html(APP_HTML)
            return
        if route == "/api/candidates":
            self.send_json({"candidates": read_index(self.server.paths.index_path), "labels": read_labels(self.server.paths.labels_path)})
            return
        if route.startswith("/api/conversation/"):
            conversation_id = urllib.parse.unquote(route.removeprefix("/api/conversation/"))
            detail = load_conversation_detail(self.server.paths, conversation_id)
            if not detail:
                self.send_error_json(HTTPStatus.NOT_FOUND, "Conversation not found.")
                return
            self.send_json(detail)
            return
        if route == "/api/paths":
            self.send_json(
                {
                    "export_dir": str(self.server.paths.export_dir),
                    "derived_dir": str(self.server.paths.derived_dir),
                    "index_path": str(self.server.paths.index_path),
                    "labels_path": str(self.server.paths.labels_path),
                    "csv_path": str(self.server.paths.csv_path),
                }
            )
            return
        self.send_error_json(HTTPStatus.NOT_FOUND, "Not found.")

    def do_POST(self) -> None:
        parsed = urllib.parse.urlparse(self.path)
        route = parsed.path
        if route.startswith("/api/labels/"):
            conversation_id = urllib.parse.unquote(route.removeprefix("/api/labels/"))
            payload = self.read_json_body()
            if payload is None:
                return
            label = sanitize_label(payload)
            labels = read_labels_document(self.server.paths.labels_path)
            label_map = labels.setdefault("labels", {})
            if label["status"] == "unread" and not label["notes"] and not label["tags"]:
                label_map.pop(conversation_id, None)
            else:
                label_map[conversation_id] = label
            write_json_atomic(self.server.paths.labels_path, labels)
            self.send_json({"ok": True, "label": label})
            return
        self.send_error_json(HTTPStatus.NOT_FOUND, "Not found.")

    def log_message(self, format: str, *args: Any) -> None:
        sys.stderr.write("%s - %s\n" % (self.address_string(), format % args))

    def read_json_body(self) -> dict[str, Any] | None:
        length_text = self.headers.get("Content-Length", "0")
        try:
            length = int(length_text)
        except ValueError:
            self.send_error_json(HTTPStatus.BAD_REQUEST, "Invalid Content-Length.")
            return None
        raw = self.rfile.read(length)
        try:
            payload = json.loads(raw.decode("utf-8"))
        except json.JSONDecodeError:
            self.send_error_json(HTTPStatus.BAD_REQUEST, "Invalid JSON.")
            return None
        if not isinstance(payload, dict):
            self.send_error_json(HTTPStatus.BAD_REQUEST, "JSON object required.")
            return None
        return payload

    def send_html(self, body: str) -> None:
        encoded = body.encode("utf-8")
        self.send_response(HTTPStatus.OK)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(encoded)))
        self.end_headers()
        self.wfile.write(encoded)

    def send_json(self, payload: Any) -> None:
        encoded = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(HTTPStatus.OK)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(encoded)))
        self.end_headers()
        self.wfile.write(encoded)

    def send_error_json(self, status: HTTPStatus, message: str) -> None:
        encoded = json.dumps({"error": message}, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(encoded)))
        self.end_headers()
        self.wfile.write(encoded)


def read_index(path: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    if not path.exists():
        return records
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            try:
                value = json.loads(line)
            except json.JSONDecodeError:
                continue
            if isinstance(value, dict):
                records.append(value)
    return records


def read_labels(path: Path) -> dict[str, Any]:
    return read_labels_document(path).get("labels", {})


def read_labels_document(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {"version": 1, "labels": {}}
    value = read_json(path)
    if not isinstance(value, dict):
        return {"version": 1, "labels": {}}
    if not isinstance(value.get("labels"), dict):
        value["labels"] = {}
    value.setdefault("version", 1)
    return value


def sanitize_label(payload: dict[str, Any]) -> dict[str, Any]:
    status = str(payload.get("status") or "unread")
    if status not in LABEL_STATUSES:
        status = "unread"
    notes = str(payload.get("notes") or "").replace("\r\n", "\n").replace("\r", "\n")
    tags_value = payload.get("tags")
    if isinstance(tags_value, list):
        tags = [str(tag).strip() for tag in tags_value if str(tag).strip()]
    else:
        tags = [tag.strip() for tag in str(tags_value or "").split(",") if tag.strip()]
    return {
        "status": status,
        "notes": notes[:5000],
        "tags": tags[:20],
        "updated_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
    }


def load_conversation_detail(paths: Paths, conversation_id: str) -> dict[str, Any] | None:
    record = next((item for item in read_index(paths.index_path) if item.get("id") == conversation_id), None)
    if not record:
        return None
    source_path = (paths.export_dir / str(record["source_file"])).resolve()
    try:
        source_path.relative_to(paths.export_dir)
    except ValueError:
        return None
    conversations = read_json(source_path)
    if not isinstance(conversations, list):
        return None
    source_index = int(record.get("source_index", -1))
    if 0 <= source_index < len(conversations):
        conversation = conversations[source_index]
        if str(conversation.get("conversation_id") or conversation.get("id")) != conversation_id:
            conversation = find_conversation(conversations, conversation_id)
    else:
        conversation = find_conversation(conversations, conversation_id)
    if not isinstance(conversation, dict):
        return None

    nodes = conversation_nodes(conversation)
    current_ids = current_path_ids(conversation, nodes)
    messages = nodes_to_messages(nodes, current_ids)
    current_messages = [message for message in messages if message.get("in_current_path")]
    visible_messages = current_messages if current_messages else messages
    for message in visible_messages:
        message.pop("created_sort", None)
    return {"record": record, "messages": visible_messages}


def find_conversation(conversations: list[Any], conversation_id: str) -> dict[str, Any] | None:
    for conversation in conversations:
        if not isinstance(conversation, dict):
            continue
        if str(conversation.get("conversation_id") or conversation.get("id")) == conversation_id:
            return conversation
    return None


def role_label(role: str) -> str:
    labels = {
        "user": "自分",
        "assistant": "ChatGPT",
        "system": "system",
        "tool": "tool",
    }
    return labels.get(role, role or "unknown")


def read_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def write_json_atomic(path: Path, payload: Any) -> None:
    tmp_path = path.with_suffix(path.suffix + ".tmp")
    with tmp_path.open("w", encoding="utf-8", newline="\n") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    os.replace(tmp_path, path)


def as_float(value: Any) -> float | None:
    if value is None:
        return None
    if isinstance(value, (int, float)):
        return float(value)
    if isinstance(value, str):
        try:
            parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
            return parsed.timestamp()
        except ValueError:
            try:
                return float(value)
            except ValueError:
                return None
    return None


def iso_from_epoch(value: float | None) -> str:
    if not value:
        return ""
    return datetime.fromtimestamp(value, timezone.utc).astimezone().replace(microsecond=0).isoformat()


APP_HTML = r"""<!doctype html>
<html lang="ja">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Career Thread Review</title>
  <style>
    :root {
      color-scheme: light;
      --bg: #f7f7f4;
      --surface: #ffffff;
      --surface-2: #f0f4f5;
      --ink: #202124;
      --muted: #626970;
      --line: #d7d9d4;
      --line-strong: #aeb6b5;
      --accent: #1f6f8b;
      --include: #0f766e;
      --maybe: #946200;
      --exclude: #9f2727;
      --unread: #5f6368;
      --mark: #fff0a6;
      --shadow: 0 10px 24px rgba(35, 40, 45, 0.08);
      --font: "Segoe UI", "Yu Gothic UI", "Meiryo", system-ui, sans-serif;
      --mono: "Cascadia Mono", Consolas, monospace;
    }
    * { box-sizing: border-box; }
    body {
      margin: 0;
      min-width: 1080px;
      background: var(--bg);
      color: var(--ink);
      font-family: var(--font);
      line-height: 1.6;
    }
    button, input, select, textarea {
      font: inherit;
    }
    button {
      min-height: 34px;
      border: 1px solid var(--line-strong);
      border-radius: 6px;
      background: var(--surface);
      color: var(--ink);
      cursor: pointer;
    }
    button:hover { border-color: var(--ink); }
    button.active {
      border-color: var(--accent);
      background: #e6f2f6;
      color: #134e62;
      font-weight: 700;
    }
    input, select, textarea {
      border: 1px solid var(--line-strong);
      border-radius: 6px;
      background: var(--surface);
      color: var(--ink);
      padding: 7px 9px;
    }
    textarea {
      width: 100%;
      min-height: 112px;
      resize: vertical;
      line-height: 1.55;
    }
    mark {
      padding: 0 2px;
      border-radius: 3px;
      background: var(--mark);
      color: inherit;
    }
    .app {
      height: 100vh;
      display: grid;
      grid-template-rows: auto minmax(0, 1fr);
    }
    .topbar {
      border-bottom: 1px solid var(--line);
      background: rgba(247, 247, 244, 0.96);
      backdrop-filter: blur(12px);
    }
    .topbar-inner {
      padding: 12px 16px;
      display: grid;
      grid-template-columns: 270px minmax(320px, 1fr) auto;
      gap: 12px;
      align-items: center;
    }
    .brand {
      min-width: 0;
      display: grid;
      gap: 1px;
    }
    .brand-title {
      font-size: 19px;
      font-weight: 700;
      line-height: 1.2;
    }
    .brand-subtitle {
      color: var(--muted);
      font-size: 12px;
      overflow: hidden;
      white-space: nowrap;
      text-overflow: ellipsis;
    }
    .filters {
      display: grid;
      grid-template-columns: minmax(180px, 1fr) 132px 132px 132px;
      gap: 8px;
    }
    .stats {
      display: flex;
      justify-content: flex-end;
      gap: 8px;
      flex-wrap: wrap;
      font-size: 12px;
      color: var(--muted);
    }
    .stat {
      border: 1px solid var(--line);
      border-radius: 6px;
      background: var(--surface);
      padding: 4px 8px;
    }
    .layout {
      min-height: 0;
      display: grid;
      grid-template-columns: 430px minmax(0, 1fr);
      gap: 14px;
      padding: 14px 16px 16px;
    }
    .list-pane, .detail-pane {
      min-height: 0;
      border: 1px solid var(--line);
      border-radius: 8px;
      background: var(--surface);
      box-shadow: var(--shadow);
      overflow: hidden;
    }
    .list-pane {
      display: grid;
      grid-template-rows: auto minmax(0, 1fr);
    }
    .list-header {
      padding: 10px 12px;
      border-bottom: 1px solid var(--line);
      color: var(--muted);
      font-size: 12px;
      display: flex;
      justify-content: space-between;
      gap: 8px;
    }
    .candidate-list {
      overflow: auto;
    }
    .candidate {
      width: 100%;
      min-height: 0;
      display: grid;
      gap: 5px;
      padding: 10px 12px;
      border: 0;
      border-bottom: 1px solid var(--line);
      border-radius: 0;
      background: var(--surface);
      text-align: left;
    }
    .candidate:hover,
    .candidate.selected {
      background: var(--surface-2);
    }
    .candidate-title {
      font-weight: 700;
      line-height: 1.35;
      overflow-wrap: anywhere;
    }
    .candidate-meta {
      display: flex;
      gap: 7px;
      align-items: center;
      flex-wrap: wrap;
      color: var(--muted);
      font-size: 12px;
    }
    .badge {
      display: inline-flex;
      align-items: center;
      min-height: 22px;
      border: 1px solid var(--line);
      border-radius: 999px;
      padding: 1px 7px;
      background: #fafafa;
      color: var(--muted);
      font-size: 12px;
      line-height: 1.2;
    }
    .badge.include { border-color: #9fd4cb; color: var(--include); background: #e9f7f4; }
    .badge.maybe { border-color: #dfc27a; color: var(--maybe); background: #fff6db; }
    .badge.exclude { border-color: #e0aaa8; color: var(--exclude); background: #fff0ef; }
    .badge.unread { color: var(--unread); }
    .hitline {
      overflow: hidden;
      white-space: nowrap;
      text-overflow: ellipsis;
      color: var(--muted);
      font-size: 12px;
    }
    .detail-pane {
      min-width: 0;
      display: grid;
      grid-template-rows: auto minmax(0, 1fr);
      overflow: hidden;
    }
    .detail-toolbar {
      padding: 18px;
      border-bottom: 1px solid var(--line);
      background: var(--surface);
      display: grid;
      gap: 14px;
    }
    .detail-scroll {
      min-height: 0;
      overflow: auto;
    }
    .detail-content {
      padding: 18px;
      display: grid;
      gap: 14px;
    }
    .empty {
      padding: 24px;
      color: var(--muted);
    }
    .detail-head {
      display: grid;
      grid-template-columns: minmax(0, 1fr) auto;
      gap: 12px;
      align-items: start;
    }
    .detail-title {
      margin: 0;
      font-size: 22px;
      line-height: 1.28;
      overflow-wrap: anywhere;
    }
    .detail-meta {
      margin-top: 5px;
      color: var(--muted);
      font-size: 12px;
    }
    .status-buttons {
      display: grid;
      grid-template-columns: repeat(4, 86px);
      gap: 6px;
    }
    .status-buttons .include.active { border-color: var(--include); background: #e9f7f4; color: var(--include); }
    .status-buttons .maybe.active { border-color: var(--maybe); background: #fff6db; color: var(--maybe); }
    .status-buttons .exclude.active { border-color: var(--exclude); background: #fff0ef; color: var(--exclude); }
    .review-box {
      border: 1px solid var(--line);
      border-radius: 8px;
      background: #fbfbfa;
      padding: 12px;
      display: grid;
      gap: 10px;
    }
    .review-row {
      display: grid;
      grid-template-columns: minmax(0, 1fr) auto;
      gap: 8px;
      align-items: end;
    }
    .review-row label {
      display: grid;
      gap: 5px;
      color: var(--muted);
      font-size: 12px;
    }
    .messages {
      display: grid;
      gap: 12px;
    }
    .message {
      border: 1px solid var(--line);
      border-radius: 8px;
      background: var(--surface);
      overflow: hidden;
    }
    .message.user { border-left: 4px solid #0f766e; }
    .message.assistant { border-left: 4px solid #7950a8; }
    .message.system, .message.tool { border-left: 4px solid #6b7280; }
    .message-head {
      padding: 7px 10px;
      border-bottom: 1px solid var(--line);
      background: #fbfbfa;
      color: var(--muted);
      font-size: 12px;
      display: flex;
      justify-content: space-between;
      gap: 8px;
    }
    .message-text {
      margin: 0;
      padding: 12px;
      white-space: pre-wrap;
      overflow-wrap: anywhere;
      font-family: var(--font);
      font-size: 14px;
      line-height: 1.65;
    }
    .snippets {
      display: grid;
      gap: 8px;
    }
    .snippet {
      border: 1px solid var(--line);
      border-radius: 6px;
      padding: 8px 10px;
      background: #fbfbfa;
      color: #3a3d40;
      font-size: 13px;
    }
    .error {
      margin: 12px;
      border: 1px solid #e0aaa8;
      border-radius: 8px;
      background: #fff0ef;
      color: var(--exclude);
      padding: 10px 12px;
    }
  </style>
</head>
<body>
  <div class="app">
    <header class="topbar">
      <div class="topbar-inner">
        <div class="brand">
          <div class="brand-title">Career Review</div>
          <div class="brand-subtitle" id="pathInfo"></div>
        </div>
        <div class="filters">
          <input id="search" type="search" placeholder="検索">
          <select id="statusFilter">
            <option value="all">全ステータス</option>
            <option value="unread">未読</option>
            <option value="include">include</option>
            <option value="maybe">maybe</option>
            <option value="exclude">exclude</option>
          </select>
          <select id="sortBy">
            <option value="updated-desc">更新日 新しい順</option>
            <option value="score-desc">スコア 高い順</option>
            <option value="created-asc">作成日 古い順</option>
            <option value="title-asc">タイトル順</option>
          </select>
          <select id="termFilter">
            <option value="all">全ヒット語</option>
          </select>
        </div>
        <div class="stats" id="stats"></div>
      </div>
    </header>
    <main class="layout">
      <section class="list-pane">
        <div class="list-header">
          <span id="listCount">0件</span>
          <span id="saveState"></span>
        </div>
        <div class="candidate-list" id="candidateList"></div>
      </section>
      <section class="detail-pane" id="detailPane">
        <div class="empty">候補を選択してください。</div>
      </section>
    </main>
  </div>
  <script>
    const state = {
      candidates: [],
      labels: {},
      selectedId: "",
      selectedDetail: null,
      paths: null,
    };

    const els = {
      pathInfo: document.getElementById("pathInfo"),
      search: document.getElementById("search"),
      statusFilter: document.getElementById("statusFilter"),
      sortBy: document.getElementById("sortBy"),
      termFilter: document.getElementById("termFilter"),
      stats: document.getElementById("stats"),
      listCount: document.getElementById("listCount"),
      saveState: document.getElementById("saveState"),
      candidateList: document.getElementById("candidateList"),
      detailPane: document.getElementById("detailPane"),
    };

    init();

    async function init() {
      try {
        const [payload, paths] = await Promise.all([
          fetchJson("/api/candidates"),
          fetchJson("/api/paths"),
        ]);
        state.candidates = payload.candidates || [];
        state.labels = payload.labels || {};
        state.paths = paths;
        els.pathInfo.textContent = paths.derived_dir || "";
        fillTermFilter();
        bindEvents();
        render();
      } catch (error) {
        showError(error.message || String(error));
      }
    }

    function bindEvents() {
      [els.search, els.statusFilter, els.sortBy, els.termFilter].forEach((element) => {
        element.addEventListener("input", render);
        element.addEventListener("change", render);
      });
    }

    function fillTermFilter() {
      const terms = new Set();
      state.candidates.forEach((candidate) => (candidate.hit_terms || []).forEach((term) => terms.add(term)));
      Array.from(terms).sort((a, b) => a.localeCompare(b, "ja")).forEach((term) => {
        const option = document.createElement("option");
        option.value = term;
        option.textContent = term;
        els.termFilter.appendChild(option);
      });
    }

    function render() {
      const items = filteredCandidates();
      renderStats(items);
      renderList(items);
      if (state.selectedId && !items.some((item) => item.id === state.selectedId)) {
        state.selectedId = "";
        state.selectedDetail = null;
        renderEmpty();
      }
    }

    function filteredCandidates() {
      const query = els.search.value.trim().toLowerCase();
      const statusFilter = els.statusFilter.value;
      const termFilter = els.termFilter.value;
      const items = state.candidates.filter((candidate) => {
        const label = labelFor(candidate.id);
        if (statusFilter !== "all" && label.status !== statusFilter) return false;
        if (termFilter !== "all" && !(candidate.hit_terms || []).includes(termFilter)) return false;
        if (!query) return true;
        const text = [
          candidate.title,
          candidate.id,
          (candidate.hit_terms || []).join(" "),
          candidate.search_text || "",
          (candidate.snippets || []).map((snippet) => snippet.text).join(" "),
          label.notes || "",
          (label.tags || []).join(" "),
        ].join("\n").toLowerCase();
        return query.split(/\s+/).every((term) => text.includes(term));
      });
      return sortItems(items);
    }

    function sortItems(items) {
      const sortBy = els.sortBy.value;
      return items.slice().sort((a, b) => {
        if (sortBy === "score-desc") return (b.score || 0) - (a.score || 0);
        if (sortBy === "created-asc") return dateValue(a.created) - dateValue(b.created);
        if (sortBy === "title-asc") return String(a.title || "").localeCompare(String(b.title || ""), "ja");
        return dateValue(b.updated || b.created) - dateValue(a.updated || a.created);
      });
    }

    function renderStats(items) {
      const counts = { unread: 0, include: 0, maybe: 0, exclude: 0 };
      state.candidates.forEach((candidate) => {
        counts[labelFor(candidate.id).status] += 1;
      });
      els.stats.innerHTML = [
        statHtml(state.candidates.length, "候補"),
        statHtml(items.length, "表示"),
        statHtml(counts.include, "include"),
        statHtml(counts.maybe, "maybe"),
        statHtml(counts.exclude, "exclude"),
      ].join("");
      els.listCount.textContent = items.length + "件";
    }

    function statHtml(value, label) {
      return `<span class="stat">${escapeHtml(value)} ${escapeHtml(label)}</span>`;
    }

    function renderList(items) {
      els.candidateList.innerHTML = items.map((candidate) => {
        const label = labelFor(candidate.id);
        const selected = candidate.id === state.selectedId ? " selected" : "";
        const snippets = (candidate.snippets || []).map((snippet) => snippet.text).join(" / ");
        return `
          <button class="candidate${selected}" type="button" data-id="${escapeAttribute(candidate.id)}">
            <span class="candidate-title">${highlight(candidate.title || "Untitled")}</span>
            <span class="candidate-meta">
              <span class="badge ${escapeAttribute(label.status)}">${escapeHtml(label.status)}</span>
              <span>score ${escapeHtml(candidate.score || 0)}</span>
              <span>${escapeHtml(formatDate(candidate.updated || candidate.created))}</span>
              <span>${escapeHtml(candidate.message_count || 0)}件</span>
            </span>
            <span class="hitline">${escapeHtml((candidate.hit_terms || []).join(", "))}</span>
            <span class="hitline">${highlight(snippets)}</span>
          </button>
        `;
      }).join("");
      els.candidateList.querySelectorAll("[data-id]").forEach((button) => {
        button.addEventListener("click", () => selectCandidate(button.dataset.id));
      });
    }

    async function selectCandidate(id) {
      state.selectedId = id;
      state.selectedDetail = null;
      render();
      els.detailPane.innerHTML = '<div class="empty">読み込み中...</div>';
      try {
        state.selectedDetail = await fetchJson("/api/conversation/" + encodeURIComponent(id));
        renderDetail();
      } catch (error) {
        els.detailPane.innerHTML = `<div class="error">${escapeHtml(error.message || String(error))}</div>`;
      }
    }

    function renderDetail() {
      const detail = state.selectedDetail;
      if (!detail) {
        renderEmpty();
        return;
      }
      const record = detail.record;
      const label = labelFor(record.id);
      els.detailPane.innerHTML = `
        <div class="detail-toolbar">
          <div class="detail-head">
            <div>
              <h1 class="detail-title">${highlight(record.title || "Untitled")}</h1>
              <div class="detail-meta">
                ${escapeHtml(formatDate(record.created))} / ${escapeHtml(formatDate(record.updated))} /
                score ${escapeHtml(record.score || 0)} / ${escapeHtml(record.source_file)} #${escapeHtml(record.source_index)}
              </div>
            </div>
            <div class="status-buttons">
              ${statusButton("unread", label.status)}
              ${statusButton("include", label.status)}
              ${statusButton("maybe", label.status)}
              ${statusButton("exclude", label.status)}
            </div>
          </div>
          <div class="review-box">
            <div class="review-row">
              <label>タグ
                <input id="tagsInput" type="text" value="${escapeAttribute((label.tags || []).join(", "))}">
              </label>
              <button id="saveLabel" type="button">保存</button>
            </div>
            <textarea id="notesInput" placeholder="レビュー用メモ">${escapeHtml(label.notes || "")}</textarea>
          </div>
        </div>
        <div class="detail-scroll">
          <div class="detail-content">
            <div class="snippets">
              ${(record.snippets || []).map((snippet) => `<div class="snippet">${highlight(snippet.text || "")}</div>`).join("")}
            </div>
            <div class="messages">
              ${(detail.messages || []).map(messageHtml).join("")}
            </div>
          </div>
        </div>
      `;
      els.detailPane.querySelectorAll("[data-status]").forEach((button) => {
        button.addEventListener("click", () => saveCurrentLabel(button.dataset.status));
      });
      document.getElementById("saveLabel").addEventListener("click", () => saveCurrentLabel());
    }

    function statusButton(status, current) {
      const active = status === current ? " active" : "";
      return `<button class="${escapeAttribute(status)}${active}" type="button" data-status="${escapeAttribute(status)}">${escapeHtml(status)}</button>`;
    }

    function messageHtml(message) {
      return `
        <article class="message ${escapeAttribute(message.role || "unknown")}">
          <div class="message-head">
            <span>${escapeHtml(message.role_label || message.role || "")}</span>
            <span>${escapeHtml(formatDate(message.created))}</span>
          </div>
          <pre class="message-text">${highlight(message.text || "")}</pre>
        </article>
      `;
    }

    async function saveCurrentLabel(statusOverride) {
      const id = state.selectedId;
      if (!id) return;
      const existing = labelFor(id);
      const notesInput = document.getElementById("notesInput");
      const tagsInput = document.getElementById("tagsInput");
      const payload = {
        status: statusOverride || existing.status || "unread",
        notes: notesInput ? notesInput.value : existing.notes || "",
        tags: tagsInput ? tagsInput.value : (existing.tags || []).join(", "),
      };
      setSaveState("保存中...");
      try {
        const result = await postJson("/api/labels/" + encodeURIComponent(id), payload);
        state.labels[id] = result.label;
        setSaveState("保存済み");
        render();
        renderDetail();
      } catch (error) {
        setSaveState("保存失敗");
        alert(error.message || String(error));
      }
    }

    function labelFor(id) {
      return state.labels[id] || { status: "unread", notes: "", tags: [] };
    }

    function renderEmpty() {
      els.detailPane.innerHTML = '<div class="empty">候補を選択してください。</div>';
    }

    function setSaveState(text) {
      els.saveState.textContent = text;
      if (text === "保存済み") {
        window.setTimeout(() => {
          if (els.saveState.textContent === text) els.saveState.textContent = "";
        }, 1400);
      }
    }

    async function fetchJson(url) {
      const response = await fetch(url);
      const payload = await response.json();
      if (!response.ok) throw new Error(payload.error || response.statusText);
      return payload;
    }

    async function postJson(url, payload) {
      const response = await fetch(url, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
      });
      const result = await response.json();
      if (!response.ok) throw new Error(result.error || response.statusText);
      return result;
    }

    function highlight(text) {
      const terms = els.search.value.trim().split(/\s+/).filter(Boolean);
      const hitTerms = state.selectedDetail && state.selectedDetail.record ? state.selectedDetail.record.hit_terms || [] : [];
      const allTerms = Array.from(new Set([...terms, ...hitTerms])).filter(Boolean);
      if (!allTerms.length) return escapeHtml(text);
      const pattern = new RegExp("(" + allTerms.map(escapeRegex).join("|") + ")", "gi");
      return String(text).split(pattern).map((part) => {
        const matched = allTerms.some((term) => term.toLowerCase() === part.toLowerCase());
        return matched ? `<mark>${escapeHtml(part)}</mark>` : escapeHtml(part);
      }).join("");
    }

    function showError(message) {
      els.detailPane.innerHTML = `<div class="error">${escapeHtml(message)}</div>`;
    }

    function dateValue(value) {
      const date = new Date(value || 0);
      return Number.isNaN(date.getTime()) ? 0 : date.getTime();
    }

    function formatDate(value) {
      if (!value) return "";
      const date = new Date(value);
      if (Number.isNaN(date.getTime())) return "";
      return new Intl.DateTimeFormat("ja-JP", {
        year: "numeric",
        month: "2-digit",
        day: "2-digit",
        hour: "2-digit",
        minute: "2-digit",
      }).format(date);
    }

    function escapeHtml(value) {
      return String(value)
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#39;");
    }

    function escapeAttribute(value) {
      return escapeHtml(value).replace(/`/g, "&#96;");
    }

    function escapeRegex(value) {
      return value.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
    }
  </script>
</body>
</html>
"""


if __name__ == "__main__":
    raise SystemExit(main())
