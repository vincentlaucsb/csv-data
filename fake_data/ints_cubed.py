'''
 * Generate
  * A: The first 100 integers
  * C: The cubes of the first 100 integers
'''

import csv

with open('ints_cubed.csv', mode='w', newline='\n') as int_file:
    writer = csv.writer(int_file)
    
    # Header Row
    writer.writerow(['A', 'C'])
    
    for i in range(1, 101):
        writer.writerow([i, i**3])