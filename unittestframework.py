import unittest


class Test(unittest.TestCase):
    def test_first_testcase(self):  # IMPORTANT: method name will always tart with "test_"
        print("Test case run started..")
        print("This is my first test case")
        print("Test case run finished..")


if __name__ == "__main__":  # this command will execute the unit test case
    unittest.main()
