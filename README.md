# Moxymind task

This project is designed to demonstrate API test automation using Python, `httpx`, and `pytest`. The tests include scenarios for GET and POST requests.

## Prerequisites

- [Python](https://www.python.org/downloads/) (version 3.12+)
- [Poetry](https://python-poetry.org/docs/#installation) (for dependency management)
- [Make](https://www.gnu.org/software/make/) (for running tasks)

## Setup

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/your-repo.git
    cd your-repo
    ```

2. **Install dependencies using `poetry`:**

    ```bash
    poetry install
    ```

3. **Create a lock file with `poetry`:**

    ```bash
    poetry lock
    ```

## Running Tests

### Run All Tests

To run all tests in the `testsuite/` folder:

```bash
make test
```

### Run tests with external data source (command line arguments)

```bash
make test ARGS="--username='{user_name}' --userjob='{user_job}'"
```