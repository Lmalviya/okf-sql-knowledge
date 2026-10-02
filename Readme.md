# okf-sql-knowledge

A knowledge layer for SQL agents, built with [OKF (Open Knowledge Format)](https://github.com/GoogleCloudPlatform/open-knowledge-format) and tested on the public [LiveSQLBench](https://livesqlbench.ai) benchmark.

SQL agents can read a database schema, but not the business rules behind it. This project stores the schema, column descriptions and business rules as an OKF bundle that an agent can read step by step, and then measures whether that helps.

This repository accompanies the blog series **Build a Knowledge Layer for SQL Agents with OKF**.

## The series

| Part | What you build | Post |
|---|---|---|
| 1 | The problem and your first bundle: explore one database, write a small OKF bundle by hand, validate it | [Part 1](LINK-TO-PART-1) |
| 2 | The compiler: raw benchmark files → full OKF bundles for all 18 databases | Coming soon |
| 3 | The agent: navigate the bundle and write SQL, in plain Python and over MCP | Coming soon |
| 4 | The honest test: four setups, same questions, compare accuracy, tokens and cost | Coming soon |

## Requirements

- **Python 3.11 or newer**
- **Git**
- **Docker Desktop**: needed from Part 3 onward, to run the benchmark database

## Setup

### 1. Check Python and Git

macOS:

```bash
python3 --version
git --version
```

Windows (PowerShell):

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

### 2. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/okf-sql-knowledge.git
cd okf-sql-knowledge
```

### 3. Create and activate a virtual environment

macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows (PowerShell):

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

```bash
pip install -r requirements.txt
```

### 5. Download the benchmark data

We use the **Base-Lite** release of [LiveSQLBench](https://huggingface.co/datasets/birdsql/livesqlbench-base-lite): 18 databases and 270 questions, a few megabytes in total. From the project folder (same command on macOS and Windows):

```bash
git clone https://huggingface.co/datasets/birdsql/livesqlbench-base-lite data/livesqlbench-base-lite
```

Check that it worked:

```bash
ls data/livesqlbench-base-lite/disaster
```

You should see three files: `disaster_column_meaning_base.json`, `disaster_kb.jsonl` and `disaster_schema.txt`.

The correct SQL answers and test cases are not public. If you want them, request them by email as described on the [dataset page](https://huggingface.co/datasets/birdsql/livesqlbench-base-lite). They are only needed for the evaluation in Part 4.

## Repository layout

```text
okf-sql-knowledge/
├── data/
│   ├── README.md      guide to the benchmark files
│   └── livesqlbench-base-lite/   raw LiveSQLBench files (downloaded, not committed)
├── bundles/           OKF bundles
├── requirements.txt
└── README.md
```

## Data and licenses

The LiveSQLBench files are **not included** in this repository. Download them from the source, as shown in [step 5](#5-download-the-benchmark-data). LiveSQLBench data is published by the BIRD team at HKU and Google Cloud. Its license is stated as CC BY 4.0 on Hugging Face and as CC BY-SA 4.0 in the [GitHub repository](https://github.com/bird-bench/livesqlbench); we follow the stricter CC BY-SA 4.0. See [data/README.md](data/README.md) for what the files contain.

License for this repository's own code: LICENSE-TBD.