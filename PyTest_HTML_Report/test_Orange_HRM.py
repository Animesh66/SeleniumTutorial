from selenium import webdriver
import pytest
import time

class TestOrangeHRM():

    @pytest.fixture()  # this method will be executed before execution of each method
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        yield
        self.driver.close()  # this statement will be executed after execution of each method

    def test_homepage_title(self, setup):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.page_title = self.driver.title
        assert self.page_title == "OrangeHRM"
        time.sleep(5)

    def test_login(self, setup):
        self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        self.driver.find_element_by_id("txtPassword").submit()
        time.sleep(5)

# To run this file we need to type "pytest -v -s PyTest_HTML_Report/test_Orange_HRM.py" in the terminal