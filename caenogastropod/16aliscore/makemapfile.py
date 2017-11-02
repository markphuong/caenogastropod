import os
import sys
from collections import defaultdict
import multiprocessing
from os import listdir
from os.path import isfile, join


thedir = [f for f in listdir('/pylon2/bi4s86p/phuong/caenogastropod/15consensus/alignments/') if isfile(join('/pylon2/bi4s86p/phuong/caenogastropod/15consensus/alignments/', f))]


counter = 0
mapfilenum = 0

for thing in thedir:
	if '.aligned' in thing:

		if counter == 0:
			out = open('mapfile' + str(mapfilenum), 'w')
			out.write(thing + '\n')
			counter += 1
			mapfilenum += 1
		elif counter > 0 and counter < 250:
			out.write(thing + '\n')
			counter += 1
		else:
			out.write(thing + '\n')
			out.close()
			counter = 0
