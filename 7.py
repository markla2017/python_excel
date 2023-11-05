from openpyxl import Workbook, load_workbook
wb = load_workbook('files/Zeszyt1.xlsx')
ws = wb.active
ws.move_range("A1:E7", rows=2, cols=2) #przesun o 2 wiersze w prawo i 2 kolumny w dol
wb.save('files/Zeszyt2.xlsx')

