import pytest


@pytest.yield_fixture()
def setup():
    print("Open browser")
    print("Open URl before login")
    yield
    print("Close browser after login")


def test_login_by_email(setup):
    print("Login by email")


def test_login_by_facebook(setup):
    print("Login by facebook")

# To execute this test case run below in terminal
# pytest -v -s pytest_multiple_TC/multiple_tc/test_login.py