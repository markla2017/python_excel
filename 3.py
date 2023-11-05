from openpyxl import Workbook, load_workbook

# create a new workbook
wb = Workbook()
ws = wb.active
ws.title = "Data"

ws.append(['Tim', 'Is', 'Great', '!'])
ws.append(['Tom', 'Is', 'Great', '!'])
ws.append(['Jessy', 'Is', 'Great', '!'])
ws.append(['Bill', 'Is', 'Great', '!'])
ws.append(['end'])
wb.save('files/tim.xlsx')