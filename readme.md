# Stash

A lightweight CLI tool for temporarily uploading files and retrieving them from any device using a generated stash key.

Stash allows you to:

- Upload one or multiple files
- Receive a unique stash key
- Download files from any device using that key
- Optionally confirm downloads interactively

---

## 🚀 Installation

### Recommended: Install with pipx

`pipx` installs CLI tools in isolated environments.

```bash
pipx install stash
pipx ensurepath
```

After running `pipx ensurepath`, restart your terminal.

If the `stash` command is not found, ensure that `~/.local/bin` is in your `PATH`:

```bash
export PATH="$HOME/.local/bin:$PATH"
```

---

### Alternative: Install with pip

```bash
pip install stash
```

> Note: Global pip installs are not recommended unless using a virtual environment.

---

## 📦 Usage

### Upload Files

Upload one or more files:

```bash
stash upload file1.txt file2.png
```

After upload, a stash key will be generated.

---

### Informative Upload

Show detailed upload information:

```bash
stash upload file1.txt -i
```

---

### Copy Stash Key to Clipboard

```bash
stash upload file1.txt -c
```

---

### Download Files

Download using a stash key:

```bash
stash download <stash-key>
```

---

### Interactive Download

Prompt before downloading each file:

```bash
stash download <stash-key> -i
```

---

## 🔄 Example Workflow

### On Machine A

```bash
stash upload report.pdf
```

Output:

```
Stash Key: 4fj39sk2
```

### On Machine B

```bash
stash download 4fj39sk2
```

---

## ⚙️ Requirements

- Python 3.11+
- Internet connection

---

## 🛠 Troubleshooting

### Command Not Found

Check your PATH:

```bash
echo $PATH
```

If `~/.local/bin` is missing:

```bash
export PATH="$HOME/.local/bin:$PATH"
```

Restart your terminal afterward.

---

## 🧪 Development Setup

Clone the repository:

```bash
git clone <your-repo-url>
cd stash
```

Install in editable mode:

```bash
pip install -e .
```

Run:

```bash
stash upload test.txt
```

---

## 📄 License

MIT License
