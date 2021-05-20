from selenium import webdriver
from selenium.webdriver import ActionChains  # this module is imported to perform different mouse actions
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.set_page_load_timeout(20)
username = driver.find_element_by_id("txtUsername")
username.send_keys("Admin")
password = driver.find_element_by_id("txtPassword")
password.send_keys("admin123")
password.submit()
time.sleep(5)
admin = driver.find_element_by_xpath("//b[contains(text(),'Admin')]")
user_management = driver.find_element_by_xpath("//a[@id='menu_admin_UserManagement']")
user = driver.find_element_by_xpath("//a[@id='menu_admin_viewSystemUsers']")
actions = ActionChains(driver)
actions.move_to_element(admin).move_to_element(user_management).move_to_element(user).click().perform() # this will hover over to admin -> user management -> user