from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome("/Users/animeshmukherjee/PycharmProjects/pythonProject/SeleniumTutorial/drivers/chromedriver")
driver.set_page_load_timeout(15)
driver.maximize_window()  # maximize the window
driver.get("https://www.expedia.com/")  # launch the chrome browser
time.sleep(5)
driver.find_element_by_xpath("//*[@id='uitk-tabs-button-container']/li[2]/a").click()
time.sleep(2)
driver.find_element_by_class_name("uitk-faux-input").click()
time.sleep(2)
driver.find_element_by_id("location-field-leg1-origin").send_keys("NYC")
time.sleep(3)
driver.find_element_by_xpath("//*[@id='location-field-leg1-origin-menu']/div[2]/ul/li[1]/button/div/div[2]").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='location-field-leg1-destination-menu']/div[1]/button").click()
time.sleep(2)
driver.find_element_by_id("location-field-leg1-destination").send_keys("CCU")
time.sleep(3)
driver.find_element_by_xpath("//*[@id='location-field-leg1-destination-menu']/div[2]/ul/li[1]/button/div").click()
time.sleep(3)
driver.find_element_by_id("d1-btn").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='wizard-flight-tab-roundtrip']/div[2]/div[2]/div/div/div[1]/div/div[2]/div/div[2]/div[2]/div[1]/table/tbody/tr[5]/td[7]/button").click()
driver.find_element_by_xpath("//*[@id='wizard-flight-tab-roundtrip']/div[2]/div[2]/div/div/div[1]/div/div[2]/div/div[2]/div[2]/div[2]/table/tbody/tr[2]/td[5]/button").click()
time.sleep(3)
driver.find_element_by_xpath("//body/div[@id='app']/div[@id='app-layer-manager']/div[@id='app-layer-base']/div[2]/div[1]/div[1]/div[5]/div[1]/figure[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/button[1]").click()
time.sleep(3)
driver.find_element_by_xpath("//button[contains(text(),'Search')]").click()
wait = WebDriverWait(driver, 40)  # Explicit Wait
element = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'No change fee')]")))  # waiting for the given element to be clickable
element.click()
time.sleep(5)
driver.quit()
