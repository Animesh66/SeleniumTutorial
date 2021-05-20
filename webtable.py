from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.w3schools.com/html/html_tables.asp")
driver.set_page_load_timeout(20)
table_row = driver.find_elements_by_xpath("//*[@id='customers']/tbody/tr")  # this is the xpath for all rows
row_count = len(table_row)  # it will give the number of rows in the table
table_column = driver.find_elements_by_xpath("//*[@id='customers']/tbody/tr[1]/th")  # this is the xpath for all columns
column_count = len(table_column)  # it will give the number of columns in the table
# print(row_count, column_count)
for row in range(2, row_count + 1):
    for column in range(1, column_count + 1):
        data = driver.find_element_by_xpath("//*[@id='customers']/tbody/tr["+str(row)+"]/td["+str(column)+"]")
        cell_data = data.text  # this will return the value of the cell
        print(cell_data, end='           ')
    print()

