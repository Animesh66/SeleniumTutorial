from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")
driver.set_page_load_timeout(5)
driver.save_screenshot('/Users/animeshmukherjee/Desktop/Animesh/homepage.jpg')  # this statement will capture screenshot
driver.get_screenshot_as_file('/Users/animeshmukherjee/Desktop/Animesh/swaglab.png')  # this statement will capture screenshot