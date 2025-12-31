# 🛠️ Command Reference

PyToolkit utilizes a categorical command structure. Use `pytoolkit [category] --help` for details on specific tools.

## 🖥️ System (`system`)

Utility for monitoring system resources.

### `pytoolkit system sys-info info`
Displays a table with CPU usage, memory, and disk stats.

---

## 🌐 Network (`network`)

Networking and diagnostic tools.

### `pytoolkit network port-scan scan [HOST]`
Scans ports on a target host.
- `--ports`: e.g., "80,443"
- `--timeout`: seconds (default 1.0)

---

## 🔐 Crypto (`crypto`)

Cryptographic and hashing utilities.

### `pytoolkit crypto hash sum [TEXT]`
Generates a hash (SHA256, MD5) for a string.

### `pytoolkit crypto hash file [PATH]`
Generates a hash for a local file.

---

## 🎨 Format (`format`)

Data formatting and prettification.

### `pytoolkit format json-pretty json [DATA]`
Prettifies a JSON string with terminal syntax highlighting.

---

## 🎨 Graphics (`graphics`)

Visual and image processing utilities.

### `pytoolkit graphics img-resize`
Launches the **GUI Image Resizer**.
- **Features**: Drag & Drop, Batch Resizing, Aspect Ratio locking.
- **Note**: Requires a display environment (X11/Wayland).
