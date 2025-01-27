import pytest


@pytest.fixture()
def for_all_api():
    return "ALL API"


@pytest.fixture()
def for_special_api():
    return "for functional API"
