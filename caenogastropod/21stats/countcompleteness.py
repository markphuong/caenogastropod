import os
import sys

rescale  = {'all':6042, 'over50':5697, 'adnan':651}

myfasta = open(sys.argv[1] , 'r')

out = open(sys.argv[2], 'w')

for line in myfasta:
	if line == ';\n':
		break

	elif "#" in line or "begin" in line or 'datatype' in line or 'matrix' in line or line == ';\n' or 'end' in line:
		continue


	elif 'nchar' in line:
		nchar = int(line.strip().split('=')[-1][:-1]) - rescale[sys.argv[3]]
		print nchar
	else:
		myseq = line.strip()
		mylength = nchar - myseq.count('-') - myseq.count('?') - myseq.count('X') - rescale[sys.argv[3]]
#		print myseq.count('-')
#		print myseq.count('?')
		mylength = float(mylength)
#		print line[:13]
#		print mylength/573854

		if 'jgi' in line:
			out.write('jgi' + '\t' + str(mylength/nchar) + '\n') ######### modify line[:13] to change how much of the name is outputted
		else:
			out.write(line.split('\'')[1] + '\t' + str(mylength/nchar) + '\n') ######### modify line[:13] to change how much of the name is outputted
