import xlutiles
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")
driver.set_page_load_timeout(10)
username_textbox = driver.find_element_by_id("user-name")
password_textbox = driver.find_element_by_id("password")
file_path ="/Users/animeshmukherjee/Desktop/Animesh/Login_id.xlsx"  # path of the excel file
sheet = "Sheet1"
row_count = xlutiles.get_row_count(file_path, sheet)
column_count = xlutiles.get_column_count(file_path, sheet)
for row in range(2, row_count + 1):  # reading data from all rws and first column
    username = xlutiles.read_data(file_path, sheet, row, 1)  # extract all usernames
    password = xlutiles.read_data(file_path, sheet, row, 2)   # extract all passwords
    time.sleep(5)
    username_textbox.send_keys(username)  # provide the username in the username textbox
    password_textbox.send_keys(password)  # provide the password in the password textbox
    password_textbox.submit()  # click on login button
    time.sleep(6)
    if driver.find_elements_by_class_name("inventory_container"):  # if login is successful then page title should match
        print("Text Case passed")
        xlutiles.write_data(file_path, sheet, row, 3, "Correct Credential")  # updated excel with the result
        time.sleep(2)
        driver.find_element_by_id("react-burger-menu-btn").click()
        time.sleep(2)
        driver.find_element_by_id("logout_sidebar_link").click()
    else:
        print("test case is failed")
        xlutiles.write_data(file_path, sheet, row, 3, "Incorrect Credential")  # update the excel value with fail result
        username_textbox.clear()
        password_textbox.clear()
    time.sleep(3)
