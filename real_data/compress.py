# Compress 2015_StateDepartment.csv with various algorithms

import shutil
import gzip
import bz2
import lzma

# gzip
with open('2015_StateDepartment.csv', mode='rb') as infile, \
     gzip.open('compressed/2015_StateDepartment.csv.gz', mode='wb') as outfile:
     shutil.copyfileobj(infile, outfile)
     
# bzip2
with open('2015_StateDepartment.csv', mode='rb') as infile, \
     bz2.open('compressed/2015_StateDepartment.csv.bz2', mode='wb') as outfile:
     shutil.copyfileobj(infile, outfile)
     
# lzma
with open('2015_StateDepartment.csv', mode='rb') as infile, \
     lzma.open('compressed/2015_StateDepartment.csv.lzma', mode='wb') as outfile:
     shutil.copyfileobj(infile, outfile)