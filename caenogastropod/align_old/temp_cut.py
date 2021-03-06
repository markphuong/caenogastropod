import os
import sys
from collections import defaultdict
from Bio.Seq import reverse_complement


thing = sys.argv[1]

		

ID = thing.split('_')[0]

fastadict = dict()

myfasta = open(thing, 'r')

for line in myfasta:
	fastadict[line.strip()[1:]] = next(myfasta).strip()
		
myfasta.close()

myblast = open(ID + '.filtered_results', 'r')

for line in myblast:
	info = line.strip().split('\t')

	lottia = info[0]

	if '|' in lottia:
		lottia = info[0].split('|')
		if len(lottia) > 5:
			lottia = lottia[3]
		else:
			lottia=lottia[2]

	outfasta = open(lottia + '.fasta', 'a')

	if int(info[8]) > int(info[9]):
		start = int(info[9])
		end = int(info[8])
		seq = reverse_complement(fastadict[info[1]])
	else:
		start = int(info[8])
		end = int(info[9])
		seq = fastadict[info[1]]


	header = '>' + '|'.join([info[1], info[6], info[7], lottia, str(start), str(end), ID])
	outfasta.write(header + '\n')
	outfasta.write(seq + '\n')
	outfasta.close()


















