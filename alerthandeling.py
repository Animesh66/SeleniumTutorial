from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.set_page_load_timeout(15)
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
alert_button = driver.find_element_by_xpath("//button[contains(text(),'Click Me')]") # this is relative xath of click me
alert_button.click()
time.sleep(5)
driver.switch_to_alert().accept()  # this will close the pop up by clicking Ok button
driver.switch_to_alert().dismiss() # this will close the popup by clicking Cancel button

