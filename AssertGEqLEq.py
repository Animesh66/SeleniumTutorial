import unittest

class AssertGEq(unittest.TestCase):
    def test_assert_gteq(self):
        self.assertGreaterEqual(100, 10, "The number is not greater or equals to the compared one")
        self.assertLessEqual(10, 10, "The number is not less than or equals to the compared one")
        self.assertGreater(110, 10, "The number is not greater than the compared one")
        self.assertLess(9, 10, "The number is not less than the compared one")


if __name__ == "__main__":
    unittest.main()
