'''
 * Generate a CSV with 10 identical columns
 * 100 rows of the first 100 integers
'''

import csv

with open('ints.csv', mode='w', newline='\n') as int_file:
    writer = csv.writer(int_file)
    
    # Header Row
    writer.writerow(['A', 'B', 'C', 'D', 'E',
        'F', 'G', 'H', 'I', 'J'])
    
    for i in range(1, 101):
        writer.writerow([i] * 10)