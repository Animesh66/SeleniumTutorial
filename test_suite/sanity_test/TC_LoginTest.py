import unittest


class LoginTest(unittest.TestCase):
    def test_loginbyEmail(self):
        print("This is login by email test")
        self.assertTrue(True, "Test case failed")

    def test_loginbyFaceook(self):
        print("This is login by Facebook test")
        self.assertTrue(True, "Test case failed")

    def test_loginbyTweeter(self):
        print("This is login by Tweeter test")
        self.assertTrue(True, "Test case failed")


if __name__ == "__main__":
    unittest.main()
