import unittest


class AsertionIn(unittest.TestCase):
    def test_assertion_in(self):
        list_name = {"Python", "Selenium", "Java"}
        # asserIn will check and return true if the value is present in the list/dictionary/tuple or not
        self.assertIn("Python", list_name, "This value is not present in the list")
        # asserIn will check and return true if the value is NOT present in the list/dictionary/tuple or not
        self.assertNotIn("Python123", list_name, "This value is present in the list")


if __name__ == "__main__":
    unittest.main()

