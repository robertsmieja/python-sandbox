import openpyxl

# grab excel file
wb = openpyxl.load_workbook('File.xlsx')

# grab worksheet
ws = wb['Sheet1']

# get all rows in 'C'
rowsInC = ws['C']

# print each cell
for cell in rowsInC:
    print(cell.value)
