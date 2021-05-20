import openpyxl as xl

path = "/Users/animeshmukherjee/Desktop/Animesh/test_xl.xlsx"
workbook = xl.load_workbook(path)
sheet = workbook["Sheet1"]
for row in range(1,6):
    for column in range(1,4):
        cell = sheet.cell(row, column)
        cell.value = "Welcome"
print("excel written successfully")
workbook.save(path)
print("excel saved successfully")