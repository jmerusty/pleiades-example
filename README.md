# Pleiades Example

This is an example project for studying the Pleiades.
The original Pymec is different repository.

public mirror: <https://github.com/CREST-applications/pymec.git>

## Installation

### 1. Install uv

uv is a popular package manager for Python. You can easily install it and create a virtual environment for your project.
Please checkout the official uv installation guide [here](https://docs.astral.sh/uv/getting-started/installation/).

Your project dependencies are kept in your local repository, so you don't have to use Docker to prevent from polluting your environment.

for Linux and MacOS:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. Clone this repository

```bash
git clone https://github.com/jmerusty/pleiades-example.git
# option: open in vscode
code ./pleiades-example
```

### 3. Initialize the project

```bash
uv sync
```

Now, you can start your project no need to install specific version of Python or any other dependencies.

### 4. Hello

```bash
uv run ./hello.py
```

## Run Examples

First, move to the examples directory.

```bash
cd ./examples
```

- raw_worker
  
  ```bash
  uv run ./raw_worker.py
  ```

- raw_requester

  ```bash
  uv run ./raw_requester.py
  ```

## Optional

- Add the Python library

  ```bash
  uv add <package> # e.g. `uv add numpy`
  ```

- Change the Python version

  ```bash
  uv python install <version> # e.g. `uv python install 3.13`
  uv python pin <version> # e.g. `uv python pin 3.13`
  ```
