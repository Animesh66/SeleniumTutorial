from selenium import webdriver
import time
import unittest
import HtmlTestRunner  # this class will help to generate HTML report


class OrangeHRMTest(unittest.TestCase):  # this is the unittest class

    @classmethod # this is a decorator
    def setUpClass(cls):  # this method is called only once before calling any other method
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls): # this method is called only once after calling any other method
        cls.driver.quit()

    def test_home_page_title_verification(self):  # this method will verify the page title
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.set_page_load_timeout(10)
        self.page_title = self.driver.title
        self.assertEqual("orangeHRM", self.page_title, "The page title does not match")
