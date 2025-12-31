# 🗺️ PyToolkit Roadmap

This document outlines the planned tools and features for PyToolkit. Tools are categorized by their interface and status.

## 🛠️ CLI Tools (Terminal-First)

| Tool | Category | Status | Description |
| :--- | :--- | :--- | :--- |
| `sys-info` | System | ✅ Done | OS, CPU, RAM, and Disk stats. |
| `port-scan`| Network | ✅ Done | Fast TCP port scanner. |
| `json-pretty`| Format | ✅ Done | Syntax-highlighted JSON formatter. |
| `hash` | Crypto | ✅ Done | File and string hashing (SHA256, MD5). |
| `b64` | Crypto | ⏳ Planned | Base64 encoder/decoder. |
| `file-sort` | File | ⏳ Planned | Automatically organize files by extension/date. |
| `log-view` | Dev | ⏳ Planned | Tail logs with syntax highlighting and filtering. |
| `todo` | Productivity| ⏳ Planned | Simple local CLI task manager. |
| `weather` | Info | ⏳ Planned | Fetch current weather for a location. |

## 🖼️ GUI Tools (Visual-First)

For tasks that are easier with an interface, PyToolkit will launch a lightweight window.

| Tool | Category | Status | Description |
| :--- | :--- | :--- | :--- |
| `color-pick` | Graphics | ⏳ Planned | Eyedropper and HEX/RGB palette. |
| `img-resize` | Graphics | ⏳ Planned | Batch resize images with drag-and-drop. |
| `qr-gen` | Tool | ⏳ Planned | Generate and display QR codes. |
| `db-explorer` | Dev | ⏳ Planned | SQLite database viewer. |
| `diff-view` | Dev | ⏳ Planned | Visual file comparison. |

---

## 🏗️ Infrastructure Roadmap

- [ ] **Full Test Suite**: 100% coverage for registry and core logic using `pytest`.
- [ ] **GitHub Actions**:
    - [ ] `CI`: Automated linting and testing.
    - [ ] `CD`: Multi-platform binary releases.
- [ ] **Plugin System**: Allow users to load tools from external locations.
- [ ] **Interactive Shell**: A repl-like experience for PyToolkit.
