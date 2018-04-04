#a simple script to find the timeseries needed and move it into the correct folder
import os
import glob
import sys
import fnmatch
import shutil

basedir='/projects/niblab/scripts/HCP_sugar'

with open(os.path.join(basedir,'blood_sugar_high.txt'),'r') as f:
    lines = f.read().splitlines()

a=glob.glob(os.path.join(basedir,'high_sug','*.txt'))
y=[]
for item in a:
	x=item.split('/')[6].strip('.txt')
	y.append(x)
def returnNotMatches(a, b):
    return [[x for x in a if x not in b], [x for x in b if x not in a]]

final= returnNotMatches(y, lines)
print final
print len(final[1])

