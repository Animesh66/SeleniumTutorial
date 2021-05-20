from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
driver.set_page_load_timeout(10)
source = driver.find_element_by_xpath("//p[contains(text(),'Drag me to my target')]")
destination = driver.find_element_by_xpath("//p[contains(text(),'Drop here')]")
action = ActionChains(driver)
action.drag_and_drop(source, destination).perform()
