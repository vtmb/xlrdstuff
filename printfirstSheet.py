import xlrd

workbook = xlrd.open_workbook("someExcel.xls")

listSheet = workbook.sheet_by_index(0)

total_rows = listSheet.nrows
total_cols = listSheet.ncols

table = list()
record = list()

for x in range(total_rows):
    for y in range(total_cols):
        record.append(listSheet.cell(x, y).value)
    table.append(record)
    record = []
    x += 1

print(table)
