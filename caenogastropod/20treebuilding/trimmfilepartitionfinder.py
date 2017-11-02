import os
import sys


mynexus = open(sys.argv[1], 'r')

out = open(sys.argv[2], 'w')

counter = 0
for line in mynexus:
	if 'end;' in line:
		out.write(line)
		break
	elif '\'' in line:

		info = line.strip().split('\'')
		info[-1] = info[-1].replace('-', '?').replace('X', '?')

		info[-2] = str(counter)
		counter += 1
		
		out.write('\''.join(info) + '\n')
	elif 'jgi' in line:
		line = line.replace('jgi', '\'jgi\'')
		info = line.strip().split('\'')
		info[-1] = info[-1].replace('-', '?').replace('X', '?')
		
		out.write('\''.join(info).replace('\'','') + '\n')
	else:
		out.write(line)