import unittest


class SkipTest(unittest.TestCase):

    def test_complete_mehod(self):  # IMPORTANT: method name will always tart with "test_"
        print("This method is completed")

    @unittest.SkipTest  # this decorator will skip this method
    def test_incomplete_method(self):
        print("this method is not yet completed")

    @unittest.skip("Skipped due to partially complete")  # skip test case execution with a comment
    def test_partially_completed(self):
        print("This method is partially completed")

    def test_complete_another(self):
        print("This method is also completed")

    @unittest.skipIf(1 == 1, "Condition is false")  # skip method if the condition is true
    def test_another_partial(self):
        print("this is another partial completed method")

    def test_another_complete(self):
        print("this is another completed method")


if __name__ == '__main__':
    unittest.main()
