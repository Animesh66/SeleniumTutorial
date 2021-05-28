import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
import pytest
import time


# this decorator will set the severity of the class it can be NORMAL, BLOCKER, CRITICAL or MINOR
@allure.severity(allure.severity_level.NORMAL)
class TestHRM():

    @allure.severity(allure.severity_level.MINOR)
    def test_logo(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.set_page_load_timeout(10)
        status = self.driver.find_element_by_xpath("//*[@id='divLogo']/img").is_displayed()
        if status:
            assert True
        else:
            assert False
        self.driver.close()

    @allure.severity(allure.severity_level.NORMAL)
    def test_list_employees(self):
        pytest.skip("Will be implemented later")

    @allure.severity(allure.severity_level.CRITICAL)
    def test_login(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.set_page_load_timeout(10)
        self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        self.driver.find_element_by_id("txtPassword").submit()
        time.sleep(3)
        self.actual_title = self.driver.title
        if self.actual_title == "OrangeHRM123":
            self.driver.close()
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="test_login_screen",
                          attachment_type=AttachmentType.PNG)
            # the above statement will capture the screenshot and save it by the name and attachment type will be PNG
            self.driver.close()
            assert False

# to run the program in terminal write "pytest -v -s Allure_Report/allure_report/test_allure_report.py"