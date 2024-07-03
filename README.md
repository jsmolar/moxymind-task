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

### Run All API Tests

To run all tests in the `testsuite/api` folder:

```bash
poetry run pytest testsuite/api
```

### Run tests with external data source (command line arguments)

```bash
poetry run pytest --username='{}' --userjob='{}'
```

### Run All UI Tests

Run Chrome standalone container. For more info see: https://github.com/SeleniumHQ/docker-selenium

```bash
docker run -p 4444:4444 -p 7900:7900 --shm-size="2g" selenium/standalone-chrome:4.22.0-20240621
```

Run all tests in the `testsuite/ui` folder:

```bash
poetry run pytest testsuite/ui
```