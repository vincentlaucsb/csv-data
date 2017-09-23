'''
 * Generate a CSV with 10 identical columns
 * 100 rows of the first 100 integers
 * Adds a useless row of metadata after the header
'''

import csv

with open('ints_skipline.csv', mode='w', newline='\n') as int_file:
    writer = csv.writer(int_file)
    
    # Header Row
    writer.writerow(['A', 'B', 'C', 'D', 'E',
        'F', 'G', 'H', 'I', 'J'])
        
    # Useless row
    writer.writerow(["100 Integers"] * 10)
    
    for i in range(1, 101):
        writer.writerow([i] * 10)