'''
 * Generate
  * A: The first 100 integers
  * B: The squares of the first 100 integers
'''

import csv

with open('ints_squared.csv', mode='w', newline='\n') as int_file:
    writer = csv.writer(int_file)
    
    # Header Row
    writer.writerow(['A', 'B'])
    
    for i in range(1, 101):
        writer.writerow([i, i**2])