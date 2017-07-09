#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Complete the 'extract_airports()' function so that it returns a list of airport
codes, excluding any combinations like "All".

Refer to the 'options.html' file in the tab above for a stripped down version
of what is actually on the website. The test() assertions are based on the
given file.
"""

from bs4 import BeautifulSoup
html_page = "options.html"

def options(soup, id):
    value_list = []
    carrier_list = soup.find(id=id)

    for option in carrier_list.find_all('option'):
        if option['value'] not in (['AllMajors','AllOthers','All']):
            value_list.append(option['value'])
    return value_list


def extract_airports(page):
    data = []
    with open(page, "r") as html:
        # do something here to find the necessary values
        soup = BeautifulSoup(html, "lxml")
        data = options(soup, 'AirportList')
        print data
    return data


def main():
    data = extract_airports(html_page)
    assert len(data) == 15
    assert "ATL" in data
    assert "ABR" in data

if __name__ == "__main__":
    main()