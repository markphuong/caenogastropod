import os
import sys

mypep = open(sys.argv[1], 'r')


out = open(sys.argv[2], 'w')

for line in mypep:
	if ">" in line:
		info = line.strip().split(' ')

		gene = info[0].split('::')[0][1:]

		length = info[-3].replace(':','=')


		header = '>' + info[0].split('::')[1] + '|' + gene + '|' + length + '\n'

		out.write(header)
	else:
		out.write(line)