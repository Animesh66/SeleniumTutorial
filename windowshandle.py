from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://demo.automationtesting.in/Windows.html")
driver.set_page_load_timeout(15)
click_button = driver.find_element_by_xpath("//body/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/a[1]/button[1]")
click_button.click()
current_handle = driver.current_window_handle
handles = driver.window_handles
for handle in handles:
    driver.switch_to.window(handle)
    time.sleep(2)
    if handle == current_handle:
        driver.close()