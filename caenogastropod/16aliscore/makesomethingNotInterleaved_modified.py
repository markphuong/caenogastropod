#!/usr/bin/env python

import os
import sys
from collections import defaultdict


out = open(sys.argv[2], 'w')

counter = 0

mynumber = 0

outmap = open(sys.argv[1] +'.namemap', 'w')

with open(sys.argv[1]) as rfile:
	for line in rfile:
		if ">" in line:
			outmap.write(line.strip() + '\t' + str(mynumber) + '\n')

			if counter == 0:
				output = '>' + str(mynumber) + '\n'
				counter += 1
			else:
				output = "\n" + '>' + str(mynumber) + '\n'
			out.write(output)
			mynumber += 1
		else:
			line = line.strip()
			out.write(line.replace('-','?'))

out.close()
