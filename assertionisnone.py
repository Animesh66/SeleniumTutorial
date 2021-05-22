# assertIsNone and assertIsNotNone
from selenium import webdriver
import unittest


class AssertionIsNone(unittest.TestCase):
    def test_assertion_is_none(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.google.com/")
        driver.set_page_load_timeout(10)
        driver_tile = driver.title
        driver_tile = None
        self.assertIsNone(driver_tile, "The test case is failed")  # if none condition true
        self.assertIsNotNone(driver_tile, "The test case is failed")  # if not none condition is true


if __name__ == "__main__":
    unittest.main()