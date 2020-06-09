def make_directory(path, foldername):
    import os

    try:
        os.mkdir(os.path.join(path, foldername))
    except:
        pass
    
def save_to_excel(workbook, sheet, row, data):
    import datetime
    import os
    import xlwt 
    from xlwt import Workbook

    # Filename
    today = str(datetime.date.today())
    workbook_filename = 'Results {}.xls'.format(today)
    
    # First row (just once)
    try:
        # Filename
        sheet.write(0, 0, 'Filename')
        # Mean (full range)
        sheet.write(0, 1, 'Mean [N]')
        # Median (full range)
        sheet.write(0, 2, 'Median [N]')
        # Standard deviation (full range)
        sheet.write(0, 3, 'Std [N]')
        # Max (full range)
        sheet.write(0, 4, 'Max [N]')
    except:
        pass
    
    # Files' rows
    # Filename
    sheet.write(row, 0, data[0]) 
    # Mean (full range)
    sheet.write(row, 1, data[1])
    # Median (full range)
    sheet.write(row, 2, data[2])
    # Standard deviation (full range)
    sheet.write(row, 3, data[3])
    # Max (full range)
    sheet.write(row, 4, data[4])
    
    workbook.save(os.path.join("data", workbook_filename))