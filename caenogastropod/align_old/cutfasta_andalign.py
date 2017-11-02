import os
import sys
from collections import defaultdict
from Bio.Seq import reverse_complement
import multiprocessing

thedir = [f for f in os.listdir('.') if os.path.isfile(f)]


for thing in thedir:
	if 'loci_v2.fa' in thing or 'Lotgi1' in thing:
		

		myfasta = open(thing, 'r')

		alreadyseen = []

		for line in myfasta:
			if ">" in line:
				seq=next(myfasta).strip()
				info = line.strip().split('|')
				if len(info) > 5:
		
					if int(info[-2]) > int(info[-1]):
						seq = reverse_complement(seq) 
					else:
						seq = seq

					locus = info[-5]
				else:
					locus = info[2]


				out = open(locus + '.transcriptfasta', 'a')


				out.write(line)
				out.write(seq + '\n')


				out.close()



	


























