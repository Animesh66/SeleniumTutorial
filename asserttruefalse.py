from selenium import webdriver
import unittest


class AssertTrueFalse(unittest.TestCase):
    def test_assert_true_false(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.google.com/")
        driver.set_page_load_timeout(10)
        webpage_title = driver.title
        #  Assert true and false
        self.assertTrue(webpage_title == "Google", "Test case is failed")
        self.assertFalse(webpage_title == "Google123", "Test case is passed")


if __name__ == "__main__":
    unittest.main()
