import os
import sys


mynamemap = open(sys.argv[1], 'r')

namedict = dict()

for line in mynamemap:
	info = line.strip().split('\t')


	namedict[info[1]] = info[0]


myfasta = open(sys.argv[2], 'r')

out = open(sys.argv[3], 'w')


for line in myfasta:
	if ">" in line:
		seq = next(myfasta).strip()

		header = namedict[line.strip()[1:]] + '\n'

		out.write(header)
		out.write(seq.replace('?', '-') + '\n')