import os

basedir='/projects/niblab/scripts/HCP_sugar'
datadir='/projects/niblab/data/HCP_PTN820/node_timeseries/3T_HCP820_MSMAll_d100_ts2'

g=os.path.join(basedir,'blood_sugar_low.txt')
h=os.path.join(basedir,'blood_sugar_high.txt')

with open(g,'r') as low_search:
	for line in low_search:
		line=line.split('\t')[0]
		print line
