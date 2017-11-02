import os
import sys


mylottia = open(sys.argv[1], 'r')

mylength = ''

origlottianame = ''
origlottiaseq = ''

for line in mylottia:
	if ">" in line:
		seq = next(mylottia).strip()
	
		origlottianame = line.strip()
		origlottiaseq = seq

		mylength = len(seq)


myblast = open(sys.argv[2], 'r')


mynewref = ''
currentlength = mylength

for line in myblast:
	info = line.strip().split('\t')

	if int(info[3]) == mylength:
		thelength = int(info[0].split('|')[-1].split('=')[-1])
#		print info[0]
#		print mylength
#		print thelength
		if thelength > currentlength:
			mynewref = info[0]
			currentlength = thelength
		else:
			continue

out = open(sys.argv[4], 'w')

if mynewref == '':
	out.write(origlottianame + '\n')
	out.write(origlottiaseq + '\n')

else:
	myfasta = open(sys.argv[3], 'r')



	for line in myfasta:
		if ">" in line:
			if line.strip()[1:] == mynewref:
				out.write(line)
				out.write(next(myfasta))
			else:
				continue

out.close()
