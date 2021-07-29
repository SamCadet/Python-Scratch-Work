import ezsheets


# ss = ezsheets.Spreadsheet('1E5mH60XFl2Lp4HfMKejjr20Z6KS5h4JH5-C6F3IvlW0')
#
# ss
#
# print(ss.title)

# ss = ezsheets.createSpreadsheet('New sheet 2')
#
# print(ss.title)

# print(ezsheets.listSpreadsheets())

# p. 343
# ss = ezsheets.Spreadsheet('1E5mH60XFl2Lp4HfMKejjr20Z6KS5h4JH5-C6F3IvlW0')
#
# print(ss.title)  # The title of the spreadsheet.
#
# ss.title = 'Class Data'  # Change the title.
#
# print(ss.spreadsheetId)  # The unique ID (this is a read-only attribute.)
# print(ss.url)  # The Original URL (this is a read-only attribute.)
# print(ss.sheetTitles)  # The titles of all the Sheet objects
# print(ss.sheets)  # The Sheet objects in this Spreadsheet, in order
# print(ss[0])  # The first Sheet object in this Spreadsheet
# Sheets can also be accessed by title.
# Sheets can also be accessed by title.
# print(ss['That get mo illa than MEEE'])
# del ss[0]  # Delete the first Sheet object in this Spreadsheet.
# The "You Don't Know NAAN" Sheet object has been deleted:
# print(ss.sheetTitles)
# ss.refresh()

# p. 344
# ss.downloadAsExcel() # Downloads the spreadsheet as an Excel file.
# ss.downloadAsODS() # Downloads the spreadsheet as an OpenOffice file.
# ss.downloadAsCSV() # Only downloads the first sheet as a CSV file.
# ss.downloadAsTSV() # Only downloads the first sheet as a TSV file.
# ss.downloadAsPDF() # Downloads the spreadsheet as a PDF.
# ss.downloadAsHTML() # Downloads the spreadsheet as a ZIP of HTML files.

# ss.delete() # Delete the spreadsheet.
# print(ezsheets.listSpreadsheets())

# p. 345

# ss = ezsheets.Spreadsheet('1E5mH60XFl2Lp4HfMKejjr20Z6KS5h4JH5-C6F3IvlW0')
# print(ss.sheets)
# print(ss.sheets[0])
# print(ss[0])  # Also gets the first Sheet object in this Spreadsheet.

# The titles of all the Sheet objects in this Spreadsheet.)
# print(ss.sheetTitles)
# print(ss['And you don\'t know NAAN'])  # Sheets can also be accessed by title.

# p.346

# ss = ezsheets.createSpreadsheet('My Spreadsheet')
# sheet = ss[0]  # Get the first sheet in this spreadsheet.
# print(sheet.title)
# sheet = ss[0]
# sheet['A1'] = 'Name'  # Set the value in cell A1.
# sheet['B1'] = 'Age'
# sheet['C1'] = 'Favorite Movie'
# sheet['A1']  # Read the value in cell A1.
# sheet['A2']  # Empty cells return a blank string.
# sheet[2, 1]  # Column 2, Row 1 is the same address as B1.
# sheet['A2'] = 'Alice'
# sheet['B2'] = 30
# sheet['C2'] = 'RoboCop'

# p. 347
# ss = ezsheets.Spreadsheet('1ZvPWT-xakmDJOMbRj-VtHvASTkMJNZ3sveKC_4batGs')
# print(ezsheets.convertAddress('A2'))  # Converts addresses...
# print(ezsheets.convertAddress(1, 2))  # ...and converts them back, too.
# print(ezsheets.getColumnLetterOf(2))
# print(ezsheets.getColumnNumberOf('B'))
# print(ezsheets.getColumnLetterOf(999))
# print(ezsheets.getColumnNumberOf('ZZZ'))

# p. 348
# ss = ezsheets.upload('produceSales.xlsx')
# ss = ezsheets.Spreadsheet('1kObqmeuYzHWK633tHPOpQUrj0SMH_BYKGERrDOV3tTQ')
# sheet = ss[0]
# print(sheet.getRow(1))  # The first row is row 1, not row 0.
# print(sheet.getRow(2))
# column_one = sheet.getColumn(1)
# print(sheet.getColumn(1))
# print(sheet.getColumn('A'))  # Same result as getColumn(1)
# print(sheet.getRow(3))
# sheet.updateRow(3, ['Pumpkin', '11.50', '20', '230'])
# print(sheet.getRow(3))
# column_one = sheet.getColumn(1)
# for i, value in enumerate(column_one):
#     # Make the Python list contain uppercase strings:
#     column_one[i] = value.upper()

# sheet.updateColumn(1, column_one)  # Update the entire column in one request.
# rows = sheet.getRows()  # Get every row in the spreadsheet.
# print(rows[0])  # Examine the values in the first row.
# print(rows[1])
# rows[1][0] = 'PUMPKIN'  # Change the produce name.
# print(rows[1])
# print(rows[10])
# rows[10][2] = '400'  # Change the pounds sold.
# rows[10][3] = '904'  # Change the total.
# print(rows[10])
# sheet.updateRows(rows)  # Update the online spreadhseet with the changes.
#
# print(sheet.rowCount)  # The number of rows in the sheet.
# print(sheet.columnCount)  # The number of columns in the sheet.
# sheet.columnCount = 4  # Change the number of columns to 4.
# print(sheet.columnCount)  # Now the number of columns in the sheet is 4.

# p. 350

# ss = ezsheets.createSpreadsheet('Multiple Sheets')
# print(ss.sheetTitles)
# print(ss.createSheet('Spam'))  # Create a new sheet at the end of the list of
# print(ss.createSheet('Eggs'))  # Create another new sheet.
# print(ss.sheetTitles)
# # Create a sheet at index 0 in the list of sheets.
# ss.createSheet('Bacon', 0)
# print(ss.sheetTitles)

# p. 351

# ss = ezsheets.Spreadsheet('1Wn8Ghl9re6Gcll-xBOzf5rGPuUisP2f6_SSuPwQeYWM')
# print(ss.sheetTitles)
# ss[0].delete()  # Delete the sheet at index 0: the "Bacon" sheet.
# print(ss.sheetTitles)
# ss['Spam'].delete()  # Delete the "Spam" sheet.
# print(ss.sheetTitles)
# sheet = ss['Eggs']  # Assign a variable to the "Eggs" sheet.
# sheet.delete()  # Delete the "Eggs" sheet.
# print(ss.sheetTitles)
# ss[0].clear()  # Clear all the cells on the "Sheet1" sheet.
# print(ss.sheetTitles)  # The "Sheet1" sheet is empty but still exists.

# p. 352

# ss1 = ezsheets.createSpreadsheet('First Spreadsheet')
# ss2 = ezsheets.createSpreadsheet('Second Spreadsheet')
# print(ss1[0])
# ss1[0].updateRow(1, ['Some', 'data', 'in', 'the', 'first', 'row'])
# ss1[0].copyTo(ss2) # Copy the ss1's Sheet1 to the ss2 spreadsheet.
# print(ss2.sheetTitles) # ss2 now contains a copy of ss1's Sheet1.
