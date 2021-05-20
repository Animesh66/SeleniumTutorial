from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.set_page_load_timeout(15)
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")
driver.switch_to.frame("packageListFrame") # frame name is specified
frame_linktext1 = driver.find_element_by_link_text("org.openqa.selenium.cli") #open link on the above frameanem
frame_linktext1.click()
time.sleep(3)
driver.switch_to.default_content() # this will return to the main page
driver.switch_to.frame("packageFrame")
driver.find_element_by_link_text("CliCommand").click()
time.sleep(3)
driver.switch_to.default_content()  # this will return to the main page
driver.switch_to.frame("classFrame")  # this is another frame name
frame_linktext2 = driver.find_element_by_link_text("CliCommand.Executable") # click on the link in the classframe
frame_linktext2.click()
time.sleep(3)
