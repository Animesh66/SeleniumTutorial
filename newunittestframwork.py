import unittest
from selenium import webdriver


class SearchEngine(unittest.TestCase):
    def test_google(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.google.com/")
        print("The title of the page is: " + self.driver.title)
        self.driver.close()

    def test_bing(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.bing.com/")
        print("The title of the page is: " + self.driver.title)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()