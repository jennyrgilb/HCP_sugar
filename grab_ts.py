#a simple script to find the timeseries needed and move it into the correct folder
import os
import glob
import sys
import fnmatch
import shutil

basedir='/projects/niblab/scripts/HCP_sugar'
datadir='/projects/niblab/data/HCP_PTN1200/node_timeseries/3T_HCP1200_MSMAll_d15_ts2'

g=os.path.join(basedir,'blood_sugar_low_j.txt')
h=os.path.join(basedir,'blood_sugar_high_j.txt')

for file in glob.glob(os.path.join(datadir,'*.txt')):
	sub0=file.split('/')[7]
	sub=sub0.strip('.txt')
	with open(g,'r') as low_search:
		print "searching"
		for line in low_search:
			line=line.split('\t')[0]
			line=line.strip('\n')
			print 'comparing '+line+' '+sub
			if fnmatch.fnmatch(sub,line):
				print "coping "+sub+" to low sugar folder"
				shutil.copy(file,os.path.join(basedir,'low_sug'))
	with open(h,'r') as hi_search:
		print "searching"
		for hiline in hi_search:
			hiline=hiline.split('\t')[0]
			hiline=hiline.strip('\n')
			print 'comparing '+hiline+' '+sub
			if fnmatch.fnmatch(sub,hiline):
				print "coping "+sub+" to low sugar folder"
				shutil.copy(file,os.path.join(basedir,'high_sug'))

