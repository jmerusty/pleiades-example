# Pleiades Example

This is an example project for studying the Pleiades.

## Installation

## 1. Install uv

uv is a popular package manager for Python. You can easily install it and create a virtual environment for your project.
Please checkout the official uv installation guide [here](https://docs.astral.sh/uv/getting-started/installation/).

Your project dependencies are kept in your local repository, so you don't have to use Docker to pollute your environment.

for Linux and MacOS:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## 2. Clone this repository

```bash
git clone https://git.dolylab.cc/mec/pymec.git
```

## 3. Initialize the project

```bash
uv sync
```

Now, you can start your project no need to install specific version of Python or any other dependencies.

## Run Examples

```bash
cd ./examples
```

- raw_worker
  
  ```bash
  uv run raw_worker.py
  ```

- raw_requester

  ```bash
  uv run raw_requester.py
  ```