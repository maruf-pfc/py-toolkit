# 🛠️ Command Reference

PyToolkit provides several subcommands for different tasks. Use `pytoolkit --help` for a full list.

## 🖥️ System (`sys-info`)

Utility for monitoring system resources.

### `pytoolkit sys-info info`

Displays a table with:
- CPU Usage (%)
- CPU Cores (logical count)
- Total and Used Memory
- Disk Usage

## 🌐 Network (`network`)

Networking tools.

### `pytoolkit network scan [HOST]`

Scans common ports on a target host.
- **Options**:
    - `--ports`: Comma-separated list of ports (default: 80,443,22,3306).
    - `--timeout`: Connection timeout in seconds (default: 1.0).

## 🔐 Crypto (`crypto`)

Hashing and cryptographic tools.

### `pytoolkit crypto sum [TEXT]`

Generates a hash for a string.
- **Options**:
    - `--algo`: Algorithm (sha256, md5, sha1).

### `pytoolkit crypto file [PATH]`

Generates a hash for a file (reads in chunks for large files).

## 🎨 Format (`format`)

Data formatting utilities.

### `pytoolkit format json [DATA]`

Prettifies a JSON string with syntax highlighting.
