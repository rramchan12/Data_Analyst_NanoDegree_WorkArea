# -*- coding: utf-8 -*-
'''
Find the time and value of max load for each of the regions
COAST, EAST, FAR_WEST, NORTH, NORTH_C, SOUTHERN, SOUTH_C, WEST
and write the result out in a csv file, using pipe character | as the delimiter.

An example output can be seen in the "example.csv" file.
'''

import xlrd
import os
import csv
from zipfile import ZipFile

datafile = "2013_ERCOT_Hourly_Load_Data"
outfile = "2013_Max_Loads.csv"


def open_zip(datafile):
    with ZipFile('{0}.zip'.format(datafile), 'r') as myzip:
        myzip.extractall()


def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile+'.xls')
    sheet = workbook.sheet_by_index(0)
    data = []
    sheet_data = [[sheet.cell_value(r, col) for col in range(2)] for r in range(sheet.nrows)]
    time_data = sheet.col_values(0, start_rowx=1, end_rowx=None)
    coast_data = sheet.col_values(1, start_rowx=1, end_rowx=None)
    east_data = sheet.col_values(2, start_rowx=1, end_rowx=None)
    far_west_data = sheet.col_values(3, start_rowx=1, end_rowx=None)
    north_data= sheet.col_values(4, start_rowx=1, end_rowx=None)
    north_c_data= sheet.col_values(5, start_rowx=1, end_rowx=None)
    southern_data= sheet.col_values(6, start_rowx=1, end_rowx=None)
    south_c_data= sheet.col_values(7, start_rowx=1, end_rowx=None)
    west_data= sheet.col_values(8, start_rowx=1, end_rowx=None)
    ercot_data= sheet.col_values(9, start_rowx=1, end_rowx=None)

    region_list = []
    region_list.extend([coast_data,east_data,far_west_data,north_data,north_c_data,southern_data, south_c_data, west_data, ercot_data])
    print (len(region_list))
    header_row = []
    data.extend(['Station', 'Year', 'Month', 'Day', 'Hour', 'Max Load'])
    stations = ['COAST', 'EAST', 'FAR_WEST', 'NORTH',
                        'NORTH_C', 'SOUTHERN', 'SOUTH_C', 'WEST']

    for region,count in enumerate(region_list):
        max_number = max(region)
        max_number_index = region.index(max_number)+1
        #max_time = time_data[max_number_index]
        max_time = sheet.cell_value(max_number_index, 0)
        max_time = xlrd.xldate_as_tuple(max_time,0)
        #data.append[ max_time]
        print (max_number,max_time)
    # YOUR CODE HERE
    # Remember that you can use xlrd.xldate_as_tuple(sometime, 0) to convert
    # Excel date to Python tuple of (year, month, day, hour, minute, second)

    return data


def save_file(data, filename):
    with open(filename, "wb") as csv_file:
        writer = csv.writer(csv_file, delimiter='|')
        for line in data:
            writer.writerow(line)
    return None
# YOUR CODE HERE


def test():
    open_zip(datafile)
    data = parse_file(datafile)
    save_file(data, outfile)

    number_of_rows = 0
    stations = []

    ans = {'FAR_WEST': {'Max Load': '2281.2722140000024',
                        'Year': '2013',
                        'Month': '6',
                        'Day': '26',
                        'Hour': '17'}}
    correct_stations = ['COAST', 'EAST', 'FAR_WEST', 'NORTH',
                        'NORTH_C', 'SOUTHERN', 'SOUTH_C', 'WEST']
    fields = ['Year', 'Month', 'Day', 'Hour', 'Max Load']

    with open(outfile) as of:
        csvfile = csv.DictReader(of, delimiter="|")
        for line in csvfile:
            station = line['Station']
            if station == 'FAR_WEST':
                for field in fields:
                    # Check if 'Max Load' is within .1 of answer
                    if field == 'Max Load':
                        max_answer = round(float(ans[station][field]), 1)
                        max_line = round(float(line[field]), 1)
                        assert max_answer == max_line

                    # Otherwise check for equality
                    else:
                        assert ans[station][field] == line[field]

            number_of_rows += 1
            stations.append(station)

        # Output should be 8 lines not including header
        assert number_of_rows == 8

        # Check Station Names
        assert set(stations) == set(correct_stations)


if __name__ == "__main__":
    test()
