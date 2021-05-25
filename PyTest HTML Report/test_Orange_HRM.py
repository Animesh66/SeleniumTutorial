from selenium import webdriver
import pytest


class TestOrangeHRM():

    @pytest.fixture()  # this method will be executed before execution of each method
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_homepage_title(self, setup):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.page_title = self.driver.title
        assert  self.page_title == "OrangeHRM"