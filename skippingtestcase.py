import unittest


class SkipTest(unittest.TestCase):

    def test_complete_mehod(self):  # IMPORTANT: method name will always tart with "test_"
        print("This method is completed")

    def test_incomplete_method(self):
        print("this method is not yet completed")

    def test_partially_completed(self):
        print("This method is partially completed")

    def test_complete_another(self):
        print("This method is also completed")


if __name__ == '__main__':
    unittest.main()
