import pytest
from httpx import Client


@pytest.fixture(scope="session")
def client():
    """Creates client for reqres.in"""
    return Client(base_url="https://reqres.in/")


def pytest_addoption(parser):
    parser.addoption(
        "--username",
        action="append",
        default=["morpheus"],
        help="name of a new user",
    )
    parser.addoption(
        "--userjob",
        action="append",
        default=["leader"],
        help="job of a new user",
    )


def pytest_generate_tests(metafunc):
    if "username" in metafunc.fixturenames:
        metafunc.parametrize("username", metafunc.config.getoption("username"))
    if "userjob" in metafunc.fixturenames:
        metafunc.parametrize("userjob", metafunc.config.getoption("userjob"))
