import os
import sys

myfile = open('adapters_reversed.fa', 'r')

out = open('adapters_reversed_changed_headers.fa', 'w')

for line in myfile:
	if ">" in line:
		out.write(line.strip() + 'r' + '\n')
	else:
		out.write(line)