from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
driver.set_page_load_timeout(20)
copy_text = driver.find_element_by_xpath("//button[contains(text(),'Copy Text')]")
action = ActionChains(driver)  # create an object of class ActionChains
action.double_click(copy_text).perform()  # this will double click on Copy Text button