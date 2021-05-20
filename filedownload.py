from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

chrome_optns = Options()
chrome_optns.add_experimental_option("prefs", {"download.default_directory":
                                                "/Users/animeshmukherjee/Desktop/Animesh/Selenium_Download"})
# this will change the default download location to the given location
driver = webdriver.Chrome(chrome_options=chrome_optns)
driver.maximize_window()
driver.get("http://demo.automationtesting.in/FileDownload.html")
driver.set_page_load_timeout(15)
textbox_one = driver.find_element_by_id("textbox")
textbox_one.send_keys("I'm a pussy cat. I don't want any heart attack")
time.sleep(2)
generate_file = driver.find_element_by_id("createTxt")
generate_file.click()
time.sleep(2)
download_button = driver.find_element_by_id("link-to-download")
download_button.click()