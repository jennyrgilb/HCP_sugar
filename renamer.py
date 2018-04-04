import os
import glob
import shutil

basedir='/projects/niblab/scripts/HCP_sugar/low_sug'
newdir='/projects/niblab/scripts/HCP_sugar/all_sug'
for x in glob.glob(os.path.join(basedir,'*')):
	z=x.split('/')[6]
	y='low_'+z
	#print y
	new_name=os.path.join(newdir, y)
	#print new_name
	if os.path.exists(new_name):
		print "already moved "+y
	else:
		shutil.copy(x,new_name)
		print "moved "+y
