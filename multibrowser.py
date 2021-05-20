from selenium import webdriver
import time

driver = webdriver.Chrome("/Users/animeshmukherjee/PycharmProjects/pythonProject/SeleniumTutorial/drivers/chromedriver")
# driver = webdriver.Firefox("/Users/animeshmukherjee/PycharmProjects/pythonProject/SeleniumTutorial/drivers/geckodriver")

driver.set_page_load_timeout(10)
driver.get("http://youtube.com")  # launch the chrome browser
print(driver.title)  # print the title of the page
driver.find_element_by_name("search_query").send_keys("Digital marketing")
driver.find_element_by_xpath("//*[@id='search-icon-legacy']").click()
time.sleep(4)
# driver.close()  # close the current window of the browser
driver.quit()  # it will close the whole browser
