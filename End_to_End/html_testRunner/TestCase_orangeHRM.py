from selenium import webdriver
import time
import unittest
import HtmlTestRunner  # this class will help to generate HTML report


class OrangeHRMTest(unittest.TestCase):  # this is the unittest class

    @classmethod # this is a decorator
    def setUpClass(cls):  # this method is called only once before calling any other method
        print("Test Started...")
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):  # this method is called only once after calling any other method
        cls.driver.quit()
        print("Test Completed...")

    def test_home_page_title_verification(self):  # this method will verify the page title
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.set_page_load_timeout(15)
        self.page_title = self.driver.title
        self.assertEqual("OrangeHRM", self.page_title, "The page title does not match")

    def test_login(self):  # this  method will verify the login process
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.username_box = self.driver.find_element_by_id("txtUsername")
        self.username_box.send_keys("Admin")
        self.password_box = self.driver.find_element_by_id("txtPassword")
        self.password_box.send_keys("admin123")
        self.password_box.submit()
        time.sleep(3)
        self.page_title = self.driver.title
        self.assertEqual("OrangeHRM", self.page_title, "The page title does not match")


if __name__ == "__main__":  # this command will execute the all class methods at once
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="/Users/animeshmukherjee/Desktop/Animesh/Log_file"))
    # this command will generate one HTML report of the output file at the given folder location

# We need to run this test case in terminal with command "python3 <filename with location>"
