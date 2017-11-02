import os
import sys
from os.path import isfile, join
import numpy

def pdist(seq1, seq2):
        """Sequences must be strings, have the same length, and be aligned"""
        num = 0
        diff = 0
        for i, nucleotide in enumerate(seq1):
                couple = [nucleotide, seq2[i]]
                if couple[0] == "-" or couple[0] == 'X':
                        continue
                elif couple[1] == "-" or couple[1] == 'X':
                        continue
                elif couple[0] == couple[1]:
                        num += 1
                elif not couple[0] == couple[1]:
                        num += 1
                        diff += 1
        if num == 0:
                return 'NA'
        else:
                pdist = float(diff)/float(num)
                return pdist


ignorelist = []

failed = open('failed_tree_filter', 'r')

for line in failed:
	ignorelist.append(line.strip())

#thedir = [f for f in os.listdir('/pylon2/bi4s86p/phuong/caenogastropod/16aliscore/filtered/') if isfile(join('/pylon2/bi4s86p/phuong/caenogastropod/16aliscore/filtered/', f))]
thedir = [f for f in os.listdir('.') if os.path.isfile(f)]


pdistdict = dict()

for thing in thedir:
#        if '130484' in thing:
	if '_AA.fasta.aligned.consensus.aliscore.NI.pdist' in thing and not thing in ignorelist: 




              


######### calculate pdist


		myfasta = open(thing, 'r')

		currentdict = dict()



		for line in myfasta:
			if ">" in line:
				ID = line.strip().split('|')[0][1:]
				seq = next(myfasta).strip()
				currentdict[ID] = seq

		myfasta.close()

		alreadyseen = []

		templist = []

		for species1 in currentdict:
			for species2 in currentdict:
				ID1 = species1 + '|' + species2
				ID2 = species2 + '|' + species1

				myvalue = pdist(currentdict[species1], currentdict[species2])

				if ID1 in alreadyseen or ID2 in alreadyseen:
					continue
				else:
					alreadyseen.append(ID1)
					alreadyseen.append(ID2)

					if species1 == species2:
						continue
					elif myvalue == 'NA':
						continue
					else:
						templist.append(myvalue)


		pdistdict[thing] = numpy.mean(templist)

		
out = open('loci_distribution', 'w')

for item in pdistdict:
	out.write(item + '\t' + str(pdistdict[item]) + '\n')
					
