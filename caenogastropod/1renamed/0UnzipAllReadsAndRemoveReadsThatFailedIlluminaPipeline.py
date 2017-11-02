#!/usr/bin/env python

#this concatenates all read files into read1 and read2 files [if you get multiple read files per index from illumina]

import os
import sys
import argparse
import multiprocessing

#manip these variables

ID = '.fastq.gz' #An ID common to all fastq files

### the script

directory = '/pylon2/bi4s86p/phuong/caenogastropod/0data'


def concat(element):
	
	newname = element.split('/')
	newname = newname[-1]
	newname = newname.split('_')
	myfilename = '-'.join(newname[0:4]) + '_' +  newname[-1][:-9] + '.fq.gz'

	variables = dict(
	index = str(element),
	newfile = str(myfilename))

	commands = """
	echo "Processing {index}"
	zcat {index} | grep -A 3 '^@.* [^:]*:N:[^:]*:' | grep -v "^--$" | sed 's/ 1:N:0:.*/\\/1/g' | sed 's/ 2:N:0:.*/\\/2/g' | gzip > {newfile}
	""".format(**variables)

	cmd_list = commands.split("\n")
	for cmd in cmd_list:
		os.system(cmd)

mylist = []

for root, dirs, files in os.walk(directory):
	for filename in files:
		path = os.path.join(root, filename)
		if ID in filename:
			if 'HETERO' in filename:
				continue
			else:
				mylist.append(path)
		else:
			continue

pool = multiprocessing.Pool(40)
pool.map(concat, mylist)


