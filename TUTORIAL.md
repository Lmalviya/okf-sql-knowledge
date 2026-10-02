# Tutorial guide: follow the blog step by step

Use this guide if you want to **build the project yourself** while reading the blog series **Build a Knowledge Layer for SQL Agents with OKF**. You start from an empty folder and write every file as the posts explain.

Just want to run the finished code? Use the [README](https://github.com/Lmalviya/okf-sql-knowledge/blob/main/README.md) instead.

| Part | Post | Steps in this guide |
|---|---|---|
| 1 | [The problem and your first bundle](https://medium.com/@lmalviya/your-agents-knowledge-needs-a-file-format-meet-okf-eb6148a4872d) | [Setup](https://github.com/Lmalviya/okf-sql-knowledge#setup) |
| 2 | Coming soon | |
| 3 | Coming soon | |
| 4 | Coming soon | |

## Setup

These steps prepare an empty project for Part 1. Commands are shown for macOS and for Windows (PowerShell).

### 1. Check Python and Git

You need **Python 3.11 or newer** and **Git**.

macOS:

```bash
python3 --version
git --version
```

Windows:

```powershell
py --version
git --version
```

If something is missing or Python is older than 3.11:

| | macOS | Windows |
|---|---|---|
| Python | `brew install python@3.12` (with [Homebrew](https://brew.sh)), then use `python3.12` | `winget install Python.Python.3.12`, or the [python.org](https://www.python.org/downloads/) installer with **"Add python.exe to PATH"** ticked |
| Git | `xcode-select --install` | `winget install --id Git.Git -e` |

Open a new terminal after installing.

### 2. Create the project folder

Same commands on macOS and Windows:

```bash
mkdir okf-sql-knowledge
cd okf-sql-knowledge
mkdir data
mkdir bundles
mkdir tools
```

Run every command in the rest of this guide, and in the blog, from inside `okf-sql-knowledge`.

### 3. Create and activate a virtual environment

macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
```

If PowerShell says that running scripts is disabled, run this once, then activate again:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

Your prompt now starts with `(.venv)`. Activate the environment again whenever you open a new terminal.

### 4. Install the dependencies

Create a file called `requirements.txt` in the project folder with this content:

```text
pyyaml==6.0.3
```

Install it:

```bash
python -m pip install -r requirements.txt
```

Check that it worked:

```bash
python -c "import yaml; print(yaml.__version__)"
```

This should print `6.0.3`.

### 5. Download the benchmark data

We use the **Base-Lite** release of [LiveSQLBench](https://huggingface.co/datasets/birdsql/livesqlbench-base-lite): 18 databases and 270 questions, a few megabytes in total. Same command on macOS and Windows:

```bash
git clone https://huggingface.co/datasets/birdsql/livesqlbench-base-lite data/livesqlbench-base-lite
```

Check that it worked:

```bash
ls data/livesqlbench-base-lite/disaster
```

You should see three files: `disaster_column_meaning_base.json`, `disaster_kb.jsonl` and `disaster_schema.txt`.

### 6. Get the OKF validator

We check bundles with the validator from [okf-skills](https://github.com/scaccogatto/okf-skills) (MIT license). It's a single Python file, so we download only that file, pinned to a fixed commit so everyone gets the same results.

macOS:

```bash
curl -L -o tools/okf_validate.py https://raw.githubusercontent.com/scaccogatto/okf-skills/8e3187875e66051bb52f91a5ed27342e2c3208da/skills/validate/scripts/okf_validate.py
```

Windows (`curl.exe` is built into Windows 10 and 11):

```powershell
curl.exe -L -o tools\okf_validate.py https://raw.githubusercontent.com/scaccogatto/okf-skills/8e3187875e66051bb52f91a5ed27342e2c3208da/skills/validate/scripts/okf_validate.py
```

You'll run it later in Part 1, once you have a bundle to check.

If you ever see `ModuleNotFoundError: No module named 'yaml'`, the virtual environment isn't active. Activate it (step 3), run step 4 again, then retry.

### You're ready

Your project now looks like this:

```text
okf-sql-knowledge/
├── .venv/
├── data/
│   └── livesqlbench-base-lite/
├── bundles/          empty for now
├── tools/
│   └── okf_validate.py
└── requirements.txt
```

Go back to [the blog post](LINK-TO-PART-1) and continue with "Get the data".