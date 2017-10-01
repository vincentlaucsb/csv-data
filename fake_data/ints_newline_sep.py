''' Same as ints.csv but the record separator is a single line feed '''

import csv

with open('ints.csv', mode='r') as old_file, \
     open('ints_newline_sep.csv', mode='w', newline='\n') as new_file:
    data = old_file.read()
    new_file.write(data)