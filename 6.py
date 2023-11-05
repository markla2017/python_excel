from openpyxl import Workbook, load_workbook

wb = load_workbook('files/Zeszyt1.xlsx')
ws = wb.active

ws.insert_rows(6) # insert empty row after row 5
ws.delete_rows(7) # delete row 7

ws.insert_cols(4)
ws.delete_cols(2)

wb.save('files/Zeszyt2.xlsx')