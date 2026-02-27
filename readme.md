# Stash

A lightweight CLI tool for temporarily uploading files and retrieving them from any device using a generated stash key.

Stash allows you to:

- Upload one or multiple files
- Receive a unique stash key
- Download files from any device using that key
- Optionally confirm downloads interactively

---

## ⚙️ Requirements

- Python 3.11+
- pipx
- Internet connection

---

## 🚀 Installation

### Recommended: Install with pipx

`pipx` installs CLI tools in isolated environments.

If pipx is not installed

```bash
pip install pipx
```

```bash
pipx install git+https://github.com/u-cant-see-me/Stash.git
pipx ensurepath
```

After running `pipx ensurepath`, restart your terminal.

If the `stash` command is not found, ensure that `~/.local/bin` is in your `PATH`:

```bash
export PATH="$HOME/.local/bin:$PATH"
```

---

<!--
### Alternative: Install with pip

```bash
pip install stash
```

> Note: Global pip installs are not recommended unless using a virtual environment.

--- -->

## 📦 Usage

### Upload Files

Upload one or more files using the full command or its alias:

```bash
# Full command
stash upload file1.txt file2.png

# Alias
stash u file1.txt file2.png
```

After upload, a stash key will be generated.

You can also use normal shell features like wildcards and globbing:

```bash
# Upload all files in the current directory
stash upload *

# Upload all files in a specific folder
stash upload my_folder/*

# Upload files matching a pattern
stash upload *.pdf
```

> Note: The shell expands `*` and patterns before passing them to `stash`.

---

### Download Files

Download using a stash key:

```bash
stash download <stash-key>
```

Aliases:

```bash
stash key <stash-key>
stash k <stash-key>
```

If no storage path is configured, files will be downloaded to the current directory.

---

## ⚙️ Configuration

Stash allows you to configure backend and storage settings.

### Set Backend URL

```bash
stash config url <backend-url>
```

Alias:

```bash
stash config u <backend-url>
```

---

### Set Download Storage Path

Set a default directory where downloaded files will be saved:

```bash
stash config store /path/to/download/folder
```

If not set, files will be downloaded to the current working directory.

---

### View Current Configuration

To see the current configuration:

```bash
stash config --show
```

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
