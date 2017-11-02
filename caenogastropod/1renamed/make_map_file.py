import os
from os import listdir
from os.path import isfile, join


myfiles = [f for f in listdir(os.getcwd()) if isfile(join(os.getcwd(), f))]

out = open('mapfile_caeno', 'w')

for line in myfiles:
	if 'R1.fq.gz' in line:
		info = line.strip().split('_')[0]
		out.write(info + '\n')