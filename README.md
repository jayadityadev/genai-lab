# Environment Setup

This project uses a standard Python virtual environment and installs dependencies from `requirements.txt`.

## Prerequisites

- Python 3.10 or newer
- `git`

## Setup

1. Clone the repository:

```bash
git clone <repository-url>
cd genai-lab
```

2. Create a virtual environment:

```bash
python -m venv .venv
```

3. Activate the virtual environment.

On Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

On Windows Command Prompt:

```bat
.venv\Scripts\activate.bat
```

4. Upgrade `pip` and install the dependencies:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Notes

- The repository already includes `requirements.txt` and `pyproject.toml`, but the setup above follows the requested `venv`-based workflow.
- If PowerShell blocks activation scripts, run PowerShell as needed for your environment policy or use Command Prompt instead.