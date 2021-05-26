from selenium import webdriver
import pytest
import allure

class TestHRM():

    def test_logo(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.set_page_load_timeout(10)

    def test_listemployees(self):


    def test_login(self):
