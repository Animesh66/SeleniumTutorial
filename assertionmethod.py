import unittest
from selenium import webdriver

class Test(unittest.TestCase):
    def test_name(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.google.com/")
        self.driver.set_page_load_timeout(5)
        self.title_of_the_page = self.driver.title
        # Equal assertion added to verify the value of page title
        self.assertEqual("Google", self.title_of_the_page, "Page title does not match")
        # it will verify the site tile value with Google and accordingly test case will pass or fail
        self.assertNotEqual("Google", self.title_of_the_page, "Page title does not match")

if __name__ == "__main__":
    unittest.main()