#!/usr/bin/env python

#REQUIRES: novoalign and samtools
#REQUIRES: a map file, with first column as sample ID, and second file as which fasta it goes to. The reason you have different fastas for different samples is because of divergent mtDNA genomes
#elements in the map file are separated by a tab

#This script aligns your paired and unpaired reads to a reference using novoalign, and makes a pileup file using samtools

import os
import sys
from os.path import isfile, join
import multiprocessing


def align1(element):

	ID = element


	variables = dict(
	sample = ID
	) #name your output


	commands = """
	python reformatfiles.py {sample}_AA.fasta.aligned_analyze.fasta.namemap ALICUT_{sample}_AA.fasta.aligned_analyze.fasta.NI {sample}_AA.fasta.aligned.consensus.aliscore.NI
	cp {sample}_AA.fasta.aligned.consensus.aliscore.NI /pylon2/bi4s86p/phuong/caenogastropod/16aliscore/filtered
	""".format(**variables)

	

	cmd_list = commands.split("\n")
	for cmd in cmd_list:
		os.system(cmd)

def align2(element):

	ID = element


	variables = dict(
	sample = ID
	) #name your output


	commands = """
	python reformatfiles.py {sample}_AA.fasta.aligned_analyze.fasta.namemap {sample}_AA.fasta.aligned_analyze.fasta.NI {sample}_AA.fasta.aligned.consensus.aliscore.NI
	cp {sample}_AA.fasta.aligned.consensus.aliscore.NI /pylon2/bi4s86p/phuong/caenogastropod/16aliscore/filtered
	""".format(**variables)

	

	cmd_list = commands.split("\n")
	for cmd in cmd_list:
		os.system(cmd)




	#Make a list of lists, each list within the list will have the first and second elements of the map file that are separated by a tab


mylist1 = []

mylist2 = []

#thedir = [f for f in os.listdir('/pylon2/bi4s86p/phuong/caenogastropod/16aliscore/results/') if isfile(join('/pylon2/bi4s86p/phuong/caenogastropod/16aliscore/results/', f))]
thedir = [f for f in os.listdir('.') if os.path.isfile(f)]

for thing in thedir:
	if '_AA.fasta.aligned_analyze.fasta.namemap' in thing:
		ID = thing.split('_')[0]

		if 'ALICUT_' + ID + '_AA.fasta.aligned_analyze.fasta.NI' in thedir:
			#align1(ID)
			mylist1.append(ID)
		else:
			mylist2.append(ID)
			#align2(ID)

pool = multiprocessing.Pool(62)
pool.map(align1, mylist1)#run the function with the arguments

pool = multiprocessing.Pool(62)
pool.map(align2, mylist2)#run the function with the arguments









