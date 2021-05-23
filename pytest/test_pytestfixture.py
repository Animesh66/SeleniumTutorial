import pytest


@pytest.fixture()  # this decorator is acting as fixture. It will be executed once before every method
def setup():
    print("Execute once before every method")


def test_method_one(setup):  # this method will execute after setup method
    print("This is test method one")


def test_method_two(setup):  # this method will execute after setup method
    print("This is test method two")

# To run this file we need to type "pytest -v -s pytest/test_pytestfixture.py" in the terminal
