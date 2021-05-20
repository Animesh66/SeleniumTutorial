from selenium import webdriver
import time
import xloperation

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("")
driver.set_page_load_timeout(15)
