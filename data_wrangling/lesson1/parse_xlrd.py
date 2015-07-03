#!/usr/bin/env python
"""
Your task is as follows:
- read the provided Excel file
- find and return the min, max and average values for the COAST region
- find and return the time value for the min and max entries
- the time values should be returned as Python tuples

Please see the test function for the expected return format
"""

import xlrd

from zipfile import ZipFile

datafile = "2013_ERCOT_Hourly_Load_Data.xls"
KEYWORD = "COAST"


def open_zip(datafile):
    with ZipFile('{0}.zip'.format(datafile), 'r') as myzip:
        myzip.extractall()


def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)

    data = {
            'maxtime': (0, 0, 0, 0, 0, 0),
            'maxvalue': 0,
            'mintime': (0, 0, 0, 0, 0, 0),
            'minvalue': 0,
            'avgcoast': 0
    }
    column_index = -1
    
    for index, row_name in enumerate(sheet.row_values(0)):
        if row_name == KEYWORD:
            column_index = index
    # sanity check
    assert column_index != -1, "The keyword {0} is not contained in the given table".format(KEYWORD)

    vals = sheet.col_values(column_index)[1:]
    # return both index and value a given list. Also taking advantage of the
    # max/min defaultly measuring the 1st item for each tuple
    data["maxvalue"], index = max((v, i) for i, v in enumerate(vals))
    data["maxtime"] = xlrd.xldate_as_tuple(sheet.cell_value(index+1, 0), 0)
    data["minvalue"], index = min((v, i) for i, v in enumerate(vals))
    data["mintime"] = xlrd.xldate_as_tuple(sheet.cell_value(index+1, 0), 0)
    data["avgcoast"] = sum(vals)/len(vals)

    return data


def test():
    open_zip(datafile)
    data = parse_file(datafile)

    assert data['maxtime'] == (2013, 8, 13, 17, 0, 0)
    assert round(data['maxvalue'], 10) == round(18779.02551, 10)


test()
