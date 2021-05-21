from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.amazon.com/")
driver.set_page_load_timeout(10)

# Capture all the cookies created by browser

cookies = driver.get_cookies()  # it will store all the cookies as name value pair(dictionary)
cookies_count = len(cookies)  # it will return the total number of cookies captured by browser
print(cookies_count)
print(cookies)

# Add a new cookie

cookie_name= {'name': 'My New Cookie', 'value': '855675675'}
driver.add_cookie(cookie_name)


# Capture all the cookies after adding new cookie

cookies = driver.get_cookies()  # it will store all the cookies as name value pair(dictionary)
cookies_count = len(cookies)  # it will return the total number of cookies captured by browser
print(cookies_count)
print(cookies)

#  Delete an existing cookie

driver.delete_cookie('My New Cookie')

# Capture all the cookies after deleting the cookie

cookies = driver.get_cookies()  # it will store all the cookies as name value pair(dictionary)
cookies_count = len(cookies)  # it will return the total number of cookies captured by browser
print(cookies_count)
print(cookies)
