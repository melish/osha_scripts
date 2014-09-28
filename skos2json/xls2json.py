import xlrd
import json

workbook = xlrd.open_workbook('nace_r2.xls')
worksheet = workbook.sheet_by_name('NACE2')
num_rows = worksheet.nrows - 1
num_cells = worksheet.ncols - 1
curr_row = -1
header = []
jsoncontent = []
while curr_row < num_rows:
    curr_row += 1
    row = worksheet.row(curr_row)
    curr_cell = -1
    row = {}
    while curr_cell < num_cells:
        curr_cell += 1
        if curr_row == 0:
            header.append(worksheet.cell_value(curr_row, curr_cell))
        else:
            # Cell Types: 0=Empty, 1=Text, 2=Number, 3=Date, 4=Boolean, 5=Error, 6=Blank
            #cell_type = worksheet.cell_type(curr_row, curr_cell)
            cell_value = worksheet.cell_value(curr_row, curr_cell)
            row[header[curr_cell]] = cell_value
    if curr_row > 0:
        jsoncontent.append(row)
print header
jsonfile = open('nace2.json', 'w')
jsonfile.write(json.dumps( jsoncontent,  sort_keys=True, indent=2))

