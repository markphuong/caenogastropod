import os
import sys
from collections import defaultdict
import argparse
import multiprocessing

from os.path import isfile, join

def checkmismatch(seq1,seq2):
        """Sequences must be strings, have the same length, and be aligned"""
        out_seq = ""

	counter = 0

        for i, nucleotide in enumerate(seq1):
                couple = [nucleotide, seq2[i]]
                if couple[0] == "-" or couple[0] == 'X':
                        continue
                elif couple[1] == "-" or couple[1] == 'X':
                        continue
                elif couple[0] == couple[1]:
                        continue
                elif not couple[0] == couple[1]:
			counter += 1

        return counter






def refine_sequences(seq1, seq2, mismatches_orig):

	mydictvalues = dict()
	mydictseq = dict()

########################################## seq1 left
	mismatches = mismatches_orig

	counter = 0

	deleted = 0
	tempseq1left =seq1
	while mismatches > 0:
		tempseq1left = list(tempseq1left)
		

		if tempseq1left[counter] == '-' or tempseq1left[counter] == 'X':
			counter += 1
			mismatches = mismatches
		else:
			tempseq1left[counter] = '-'
			deleted += 1
			tempseq1left = ''.join(tempseq1left)
			mismatches = checkmismatch(tempseq1left, seq2)
			counter += 1

	mydictvalues['seq1left'] = deleted
	mydictseq['seq1left'] = create_consensus(tempseq1left, seq2)[0]

########################################## seq2 left
	mismatches = mismatches_orig
	counter = 0

	deleted = 0
	tempseq2left =seq2
	while mismatches > 1:
		tempseq2left = list(tempseq2left)
		

		if tempseq2left[counter] == '-' or tempseq2left[counter] == 'X':
			counter += 1
			mismatches = mismatches
		else:
			tempseq2left[counter] = '-'
			deleted += 1
			tempseq2left = ''.join(tempseq2left)
			mismatches = checkmismatch(tempseq2left, seq1)
			counter += 1

	mydictvalues['seq2left'] = deleted
	mydictseq['seq2left'] = create_consensus(tempseq2left, seq1)[0]


########################################## seq1 right
	mismatches = mismatches_orig
	counter = -1

	deleted = 0
	tempseq1right =seq1
	while mismatches > 1:
		tempseq1right = list(tempseq1right)
		

		if tempseq1right[counter] == '-' or tempseq1right[counter] == 'X':
			counter += -1
			mismatches = mismatches
		else:
			tempseq1right[counter] = '-'
			deleted += 1
			tempseq1right = ''.join(tempseq1right)
			mismatches = checkmismatch(tempseq1right, seq2)
			counter += -1



	mydictvalues['seq1right'] = deleted
	mydictseq['seq1right'] = create_consensus(tempseq1right, seq2)[0]

########################################## seq2 right
	mismatches = mismatches_orig
	counter = -1

	deleted = 0
	tempseq2right =seq2
	while mismatches > 1:
		tempseq2right = list(tempseq2right)
		

		if tempseq2right[counter] == '-' or tempseq2right[counter] == 'X':
			counter += -1
			mismatches = mismatches
		else:
			tempseq2right[counter] = '-'
			deleted += 1
			tempseq2right = ''.join(tempseq2right)
			mismatches = checkmismatch(tempseq2right, seq1)
			counter += -1

	mydictvalues['seq2right'] = deleted
	mydictseq['seq2right'] = create_consensus(tempseq2right, seq1)[0]


	return mydictseq[min(mydictvalues, key=mydictvalues.get)]







###### create consensus between exons in multiple sequences

def create_consensus(seq1, seq2):
        """Sequences must be strings, have the same length, and be aligned"""
        out_seq = ""

	counter = 0

        for i, nucleotide in enumerate(seq1):
                couple = [nucleotide, seq2[i]]
                if couple[0] == "-" or couple[0] == 'X':
                        out_seq += couple[1]
                elif couple[1] == "-" or couple[1] == 'X':
                        out_seq += couple[0]
                elif couple[0] == couple[1]:
                        out_seq += couple[0]
                elif not couple[0] == couple[1]:
                        out_seq += couple[0]
			counter += 1
        return [out_seq, counter]











def make_consensus(thing):
	if '_AA.fasta.aligned' in thing:
		print thing

		cmd = "python makesomethingNotInterleaved.py " + thing + " " + thing + ".NI"
		os.system(cmd)

		myfasta = open(thing + '.NI', 'r')

		fastadict = defaultdict()

		for line in myfasta:
			if ">" in line:
		
				ID = line.strip().split('|')[0][1:]

				seq = next(myfasta).strip()

				if ID in fastadict:		
					fastadict[ID].append([line, seq])
				else:
					fastadict[ID] = [[line, seq]]


		out = open(thing + '_analyze.fasta', 'w')
		for key in fastadict:
			if len(fastadict[key]) == 1:
				out.write(">" + key + '\n')
				out.write(fastadict[key][0][1] + '\n')
			else:
				mylist = fastadict[key]


				########## store sequences into a new dictionary, ordered by the first coordinate of the blast query on the lottia protein so you analyze sequences in order
				tempdict = dict()
				for item in mylist:
					tempdict[int(item[0].split('|')[-4])] = item[1]


				mytempkeys = sorted(tempdict) # holds the keys, which are the start of the blast query on the lottia protein ID taken from the fasta header

				##################### 
				n = 2
				different = 0



				consensus = create_consensus(tempdict[mytempkeys[0]], tempdict[mytempkeys[1]])

				consensus_seq = consensus[0]

				# if there are greater than 1 mismatches, trim until there are no mismatche
			
				#and you trim by trimming all 4 sides, and checking how many AAs you have to delete until they merge perfectly. the one with the least deletions gets picked

				if consensus[1] > 1:

					consensus_seq = refine_sequences(tempdict[mytempkeys[0]], tempdict[mytempkeys[1]], consensus[1])

				else:
					consensus_seq = consensus[0]
					different = consensus[1]

				while n < len(mylist):

					consensus = create_consensus(consensus_seq, tempdict[mytempkeys[n]])

					if consensus[1] > 1:
						consensus_seq = refine_sequences(consensus[0], tempdict[mytempkeys[n]], consensus[1])
					else:
												
						consensus_seq = consensus[0]
						different = different + consensus[1]

					n += 1

					

				if different > 5:
					print fastadict[key]
					out.write(">" + key + '\n')
					out.write(consensus_seq + '\n')
				else:
					out.write(">" + key + '\n')
					out.write(consensus_seq + '\n')
		out.close()

		cmd = "cp " + thing + "_analyze.fasta /pylon2/bi4s86p/phuong/caenogastropod/15consensus/alignments"
		os.system(cmd)		
		
thedir = [f for f in os.listdir('.') if os.path.isfile(f)]
mylist = []

for thing in thedir:
	if '_AA.fasta.aligned' in thing:

		mylist.append(thing)


pool = multiprocessing.Pool(62)
pool.map(make_consensus, mylist)#run the function with the arguments








