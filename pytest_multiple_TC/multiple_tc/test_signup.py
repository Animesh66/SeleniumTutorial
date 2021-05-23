import pytest


@pytest.yield_fixture()
def setup():
    print("Open browser")
    print("Open URl before signup")
    yield
    print("Close browser after signup")


def test_signup_by_email(setup):
    print("signup by email")


def test_signup_by_facebook(setup):
    print("signup by facebook")

# To execute this test case run below in terminal
# pytest -v -s pytest_multiple_TC/multiple_tc/test_signup.py