# Moxymind task

This project is designed to demonstrate API test automation using Python, `httpx`, and `pytest`. The tests include scenarios for GET and POST requests.

## Prerequisites

- [Python](https://www.python.org/downloads/) (version 3.12+)
- [Poetry](https://python-poetry.org/docs/#installation) (for dependency management)

## Setup

**Clone the repository:**

```bash
git clone https://github.com/jsmolar/moxymind-task.git
cd moxymind-task
```

## Running Tests

### Run All Tests

To run all tests in the `testsuite/` folder:

```bash
poetry run pytest
```

### Run tests with external data source (command line arguments)

```bash
poetry run pytest --username='{}' --userjob='{}'
```