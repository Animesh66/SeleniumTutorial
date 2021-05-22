import unittest


class SignupTest(unittest.TestCase):
    def test_signupbyEmail(self):
        print("This is signup by email test")
        self.assertTrue(True, "Test case failed")

    def test_signupbyFaceook(self):
        print("This is signup by Facebook test")
        self.assertTrue(True, "Test case failed")

    def test_signupbyTweeter(self):
        print("This is signup by Tweeter test")
        self.assertTrue(True, "Test case failed")


if __name__ == "__main__":
    unittest.main()