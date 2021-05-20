from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
driver.set_page_load_timeout(10)
driver.switch_to_frame(0)  # switch to fame to identify the form
upload_file = driver.find_element_by_id("RESULT_FileUpload-10")  # this command will identify the upload file button
file_path = "/Users/animeshmukherjee/Downloads/Dexter.jpeg"  # this is the file path
upload_file.send_keys(file_path)  # perform upload file process
