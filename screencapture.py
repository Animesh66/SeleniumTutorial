from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")
driver.set_page_load_timeout(10)
driver.get_screenshot_as_file("/Users/animeshmukherjee/Desktop/Animesh/screenshot/swaglabs.png")
driver.save_screenshot("/Users/animeshmukherjee/Desktop/Animesh/screenshot/testscreen.jpg")