from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.set_page_load_timeout(15)
time.sleep(3)

# 1. Scroll down by pixel number(till 1000 pixel number)

driver.execute_script("window.scrollBy(0 , 1000)", "")

# 2. Scroll down till the element found

flag = driver.find_element_by_xpath("//td[contains(text(),'India')]")
driver.execute_script("arguments[0].scrollIntoView();", flag)

# 3. Scroll down the page till end of page

driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")