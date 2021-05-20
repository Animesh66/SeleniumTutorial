from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("/Users/anime shmukherjee/PycharmProjects/pythonProject/SeleniumTutorial/drivers/chromedriver")
driver.set_page_load_timeout(10)
driver.maximize_window()  # maximize the window
driver.get("https://www.saucedemo.com/")  # launch the chrome browser
driver.implicitly_wait(10)  # this will wait till 10 seconds
username = driver.find_element_by_name("user-name")
password = driver.find_element_by_name("password")
login = driver.find_element_by_name("login-button")
if username.is_enabled():
    username.send_keys("standard_user")
else:
    print("Username is not enabled")
if password.is_enabled():
    password.send_keys("secret_sauce")
else:
    print("Password is not enabled")
if login.is_enabled():
    login.click()
else:
    print("login button is not enabled")
time.sleep(5)
# driver.close()  # close the current window of the browser
driver.quit()  # it will close the whole browser
