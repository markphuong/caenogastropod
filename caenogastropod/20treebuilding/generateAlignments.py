#!/usr/bin/env python

import os
import sys
import argparse
import multiprocessing
from Bio.Nexus import Nexus






adnanlist = []

adnan = open('adnan_loci', 'r')

for line in adnan:
	adnanlist.append(line.strip())


thedir = [f for f in os.listdir('.') if os.path.isfile(f)]


adnan_file_list = []
all_file_list = []
greater_than_50_list = []

for thing in thedir:
	if '.nexus' in thing:

		all_file_list.append(thing)

		mynexus = open(thing, 'r')

		for line in mynexus:
			if 'ntax' in line:
				myntax = int(line.split(' ')[1].split('=')[1])
				mynchar = int(line.strip().split('=')[2][:-1])
				break

		locus = thing.split('.')[0]
		if locus in adnanlist:
			adnan_file_list.append(thing)

		if myntax > 42:
			greater_than_50_list.append(thing)

		if mynchar < 10:
			print 'fuck'
			print thing
		

print 'adnan only'
print len(adnan_file_list)
print 'all'
print len(all_file_list)
print 'greater than 50'
print len(greater_than_50_list)

nexi =  [(fname, Nexus.Nexus(fname)) for fname in adnan_file_list]

combined = Nexus.combine(nexi)
combined.write_nexus_data(filename=open('adnan_only.nexus', 'w'))

nexi =  [(fname, Nexus.Nexus(fname)) for fname in all_file_list]

combined = Nexus.combine(nexi)
combined.write_nexus_data(filename=open('all_files.nexus', 'w'))

nexi =  [(fname, Nexus.Nexus(fname)) for fname in greater_than_50_list]

combined = Nexus.combine(nexi)
combined.write_nexus_data(filename=open('greater_than_50.nexus', 'w'))