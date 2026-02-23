[![PyPI - Version](https://img.shields.io/pypi/v/stash?style=for-the-badge)](https://pypi.org/project/stash/)

[![PyPI - Downloads](https://img.shields.io/pypi/dm/stash?style=for-the-badge)](https://pypi.org/project/stash/)

[![GitHub stars](https://img.shields.io/github/stars/u-cant-see-me/Stash?style=for-the-badge)](https://github.com/u-cant-see-me/Stash/stargazers)

[![GitHub forks](https://img.shields.io/github/forks/u-cant-see-me/Stash?style=for-the-badge)](https://github.com/u-cant-see-me/Stash/network)

[![GitHub issues](https://img.shields.io/github/issues/u-cant-see-me/Stash?style=for-the-badge)](https://github.com/u-cant-see-me/Stash/issues)

[![GitHub license](https://img.shields.io/github/license/u-cant-see-me/Stash?style=for-the-badge)](LICENSE) <!-- TODO: Add actual license file -->

**Effortlessly upload and download files to temporary cloud storage directly from your terminal.**

</div>

## 📖 Overview

Stash is a lightweight and powerful Command-Line Interface (CLI) tool designed to simplify the process of uploading and downloading files to a temporary cloud storage service. Built with Python, it provides a seamless and intuitive way to manage your temporary files directly from the comfort of your terminal, making it ideal for sharing quick files, transferring data between systems, or temporary backups without ever leaving your command prompt.

## ✨ Features

- 🎯 **Quick File Uploads:** Easily upload any file from your local machine to a temporary cloud storage.
- ⬇️ **Hassle-free Downloads:** Retrieve files using their unique IDs, directly to your specified local path.
- 🚀 **Intuitive CLI:** A user-friendly command-line interface powered by Typer for a smooth experience.
- 🎨 **Rich Terminal Output:** Enhanced visual feedback during operations with `rich`, including progress indicators.

## 🖥️ Screenshots

<!-- TODO: Add actual screenshots showing the CLI in action for upload and download -->

## 🛠️ Tech Stack

**CLI & Runtime:**

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)

[![Typer](https://img.shields.io/badge/Typer-0.9.0-044F69?style=for-the-badge&logo=typer&logoColor=white)](https://typer.tiangolo.com/)

[![Rich](https://img.shields.io/badge/Rich-13.7.0-darkgreen?style=for-the-badge&logo=python&logoColor=white)](https://rich.readthedocs.io/en/stable/)

[![Requests](https://img.shields.io/badge/Requests-2.31.0-blue?style=for-the-badge&logo=python&logoColor=white)](https://requests.readthedocs.io/en/latest/)

[![Python Multipart](https://img.shields.io/badge/python--multipart-0.0.6-orange?style=for-the-badge&logo=python&logoColor=white)](https://pypi.org/project/python-multipart/)

**Development Tools:**

[![Poetry](https://img.shields.io/badge/Poetry-1.x-602F8D?style=for-the-badge&logo=poetry&logoColor=white)](https://python-poetry.org/)

[![Pytest](https://img.shields.io/badge/Pytest-7.4.4-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)](https://docs.pytest.org/en/stable/)

[![Pytest Cov](https://img.shields.io/badge/Pytest--Cov-4.1.0-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)](https://pytest-cov.readthedocs.io/en/latest/)

## 🚀 Quick Start

### Prerequisites

- Python 3.10 or higher.

### Installation

You can install Stash either globally via `pip` (once published to PyPI) or by cloning the repository and setting it up with Poetry or pip for development.

#### 1. Global Installation (Recommended)

Once published to PyPI, you can install Stash globally:

```bash
pip install stash
```

#### 2. Local Installation from Source (using Poetry)

For development or if you prefer using Poetry:

1.  **Clone the repository**

    ```bash
    git clone https://github.com/u-cant-see-me/Stash.git
    cd Stash
    ```

2.  **Install Poetry (if you don't have it)**

    ```bash
    curl -sSL https://install.python-poetry.org | python -
    ```

3.  **Install dependencies**

    ```bash
    poetry install
    ```

4.  **Activate virtual environment and run**
    ```bash
    poetry shell
    stash --help
    ```

#### 3. Local Installation from Source (using pip)

1.  **Clone the repository**

    ```bash
    git clone https://github.com/u-cant-see-me/Stash.git
    cd Stash
    ```

2.  **Install dependencies**

    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the CLI (using python -m or direct execution if entry point is set)**

    ```bash
    # If package is installed in editable mode:
    pip install -e .
    stash --help

    # Alternatively, without editable install:
    python -m stash --help
    ```

### Environment setup

Before using Stash, you need to configure the API endpoint for your temporary storage service.

```bash
cp .env.example .env # Create .env if you use a local .env file manager, otherwise set directly in your shell

# Configure your environment variables:
export STASH_API_URL="https://api.your-temp-storage.com"
```

## 📁 Project Structure

```
Stash/
├── .gitignore          # Git ignore file
├── pyproject.toml      # Poetry configuration and dependency definitions
├── readme.md           # Project README file
├── requirements.txt    # Pip-compatible dependency list
└── stash/              # Main source directory for the Stash CLI tool
    └── # (Contains Python modules implementing the CLI commands and logic)
```

## ⚙️ Configuration

### Environment Variables

The CLI tool expects the following environment variable to be set:

| Variable | Description | Default | Required |

|---------------|-------------------------------------------------|----------|----------|

| `STASH_API_URL` | The base URL of the temporary file storage API. | `None` | Yes |

You can set this in your shell's profile (e.g., `.bashrc`, `.zshrc`) or before running the `stash` command.

## 📖 Usage

### Basic Commands

Run `stash --help` to see a list of available commands:

```bash
stash --help
```

### Available Commands

| Command | Description | Options/Arguments |

|------------|-----------------------------------------------|-------------------------------------------------|

| `upload` | Uploads a file to the temporary storage. | `<FILE_PATH>`: Path to the file to upload. |

| `download` | Downloads a file from the temporary storage. | `<STASH_ID>`: ID of the file to download.<br>`[OUTPUT_PATH]`: Optional path to save the downloaded file (defaults to current directory). |

### Examples

#### Upload a file

To upload a file named `my_document.pdf`:

```bash
stash upload my_document.pdf
```

The CLI will output the unique ID of the uploaded file.

#### Download a file

To download a file with the ID `abcdef123456` and save it as `downloaded_file.pdf`:

```bash
stash download abcdef123456 downloaded_file.pdf
```

If `OUTPUT_PATH` is omitted, the file will be saved in the current directory with its original name (if available from the API).

## 🔧 Development

### Available Scripts

The `pyproject.toml` defines development dependencies for testing.

| Command | Description |

|-----------------------------|------------------------------------------|

| `poetry run pytest` | Runs all unit and integration tests. |

| `poetry run pytest --cov` | Runs tests and reports code coverage. |

### Development Workflow

1.  Set up the project locally using Poetry as described in "Installation from Source".
2.  Activate the Poetry shell (`poetry shell`).
3.  Develop new features or fix bugs in the `stash/` directory.
4.  Run tests regularly to ensure functionality (`poetry run pytest`).

## 🧪 Testing

To run the test suite, navigate to the project root and use Poetry:

```bash

# Run all tests
poetry run pytest

# Run tests and generate a coverage report
poetry run pytest --cov=stash
```

## 🤝 Contributing

We welcome contributions! Please feel free to open issues or submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

### Development Setup for Contributors

Follow the "Local Installation from Source (using Poetry)" steps to set up your development environment.

## 📄 License

This project is licensed under an [Open Source License](LICENSE) - see the LICENSE file for details. <!-- TODO: Add actual license file (e.g., MIT, Apache 2.0) -->

## 🙏 Acknowledgments

- [Typer](https://typer.tiangolo.com/) for building an amazing CLI framework.
- [Rich](https://rich.readthedocs.io/) for making terminal UIs beautiful and powerful.
- [Requests](https://requests.readthedocs.io/en/latest/) for simplifying HTTP interactions.
- [Poetry](https://python-poetry.org/) for excellent Python project management.

## 📞 Support & Contact

- 🐛 Issues: [GitHub Issues](https://github.com/u-cant-see-me/Stash/issues)

---

<div align="center">

**⭐ Star this repo if you find it helpful!**

Made with ❤️ by [u-cant-see-me](https://github.com/u-cant-see-me)

</div>
