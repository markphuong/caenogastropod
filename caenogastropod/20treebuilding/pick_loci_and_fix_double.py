import os
import sys
from collections import defaultdict
import argparse

from os.path import isfile, join



###### create consensus between exons in multiple sequences

def create_consensus(seq1, seq2):
        """Sequences must be strings, have the same length, and be aligned"""
        out_seq = ""

	counter = 0

        for i, nucleotide in enumerate(seq1):
                couple = [nucleotide, seq2[i]]
                if couple[0] == "-":
                        out_seq += couple[1]
                elif couple[1] == "-":
                        out_seq += couple[0]
                elif couple[0] == couple[1]:
                        out_seq += couple[0]
                elif not couple[0] == couple[1]:
                        out_seq += couple[0]
			counter += 1
        return [out_seq, counter]


############### map sample to a species name

mymap = open('species_name_mapping', 'r')

speciesdict = dict()

for line in mymap:
        info = line.strip().split('\t')

        speciesdict[info[0]] = info[1]

######## open species to exclude




excludelist =[]

with open('excludethese') as rfile:
	for line in rfile:
		line = line.strip()
		excludelist.append(line)




thedir = [f for f in os.listdir('/pylon2/bi4s86p/phuong/exonCapNico/10fasta_and_align/aligned/') if isfile(join('/pylon2/bi4s86p/phuong/exonCapNico/10fasta_and_align/aligned/', f))]





for thing in thedir:
	if '.aligned' in thing:

		cmd = 'cp /pylon2/bi4s86p/phuong/exonCapNico/10fasta_and_align/aligned/' + thing + ' ./'
		os.system(cmd)
		cmd = "python makesomethingNotInterleaved.py " + thing + " " + thing + ".NI"
		os.system(cmd)

		myfasta = open(thing + '.NI', 'r')

		fastadict = defaultdict()




		for line in myfasta:
			if ">" in line:
				seq = next(myfasta).strip()
				if ">_R_" in line:
					ID = line.strip().split('|')[0][4:]
				else:
					ID = line.strip().split('|')[0][1:]

				if ID in excludelist:
					continue
				elif ID in fastadict:
					fastadict[ID].append([line, seq])

				else:
					fastadict[ID] = [[line, seq]]					
		

		if len(fastadict) >= int(sys.argv[1]):

			out = open(thing + '_analyze.fasta', 'w')
			for key in fastadict:
				if len(fastadict[key]) == 1:
					out.write(">" + speciesdict[key] + '\n')
					out.write(fastadict[key][0][1] + '\n')
				elif len(fastadict[key]) == 2:
			

					seq1 = fastadict[key][0][1]
					seq2 = fastadict[key][1][1]

					newinfo = create_consensus(seq1, seq2)

					if newinfo[1] > 1:
						print thing
						print len(fastadict)
						continue
					else:
						out.write(">" + speciesdict[key] + '\n')
						out.write(newinfo[0] + '\n')
				else:
					print 'fuck'

		else:
			continue







