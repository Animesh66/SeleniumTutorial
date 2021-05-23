import pytest


@pytest.yield_fixture()  # this decorator will force this function to execute before and after of mentioned test method
def tear_down():
    print("Once before every method")  # this statement will execute before execution of a function
    yield
    print("Once after every method")  # this statement will execute after execution of a function


def test_method_one(tear_down):
    print("This is one test method")


def test_method_two(tear_down):
    print("This is second est method")

