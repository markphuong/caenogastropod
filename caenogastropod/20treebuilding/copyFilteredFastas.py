#!/usr/bin/env python

#REQUIRES: novoalign and samtools
#REQUIRES: a map file, with first column as sample ID, and second file as which fasta it goes to. The reason you have different fastas for different samples is because of divergent mtDNA genomes
#elements in the map file are separated by a tab

#This script aligns your paired and unpaired reads to a reference using novoalign, and makes a pileup file using samtools

import os
import sys
import argparse
import multiprocessing
from os.path import isfile, join

#this is a wrap around for novoalign and samtools where each sample identifier was "index#" where # was a number between 1 - 50

def get_args(): #arguments needed to give to this script
	parser = argparse.ArgumentParser(description="run novoalign")

	#forces required argument to let it run
	required = parser.add_argument_group("required arguments") 
	required.add_argument("--map", help="textfile with samples to run and what fasta file to match it to", required=True) #A map file with the sample ID and the fasta file it goes to

	return parser.parse_args()

def align(element):




	variables = dict(
	sample = element
	) #name your output


	commands = """
	cp /pylon2/bi4s86p/phuong/caenogastropod/17pdist/results/{sample} /pylon2/bi4s86p/phuong/caenogastropod/20treebuilding/keptfastas/
	""".format(**variables)


	cmd_list = commands.split("\n")
	for cmd in cmd_list:
		os.system(cmd)

ignorelist = []

failed = open('failed_tree_filter', 'r')

for line in failed:
	ignorelist.append(line.strip())

#thedir = [f for f in os.listdir('.') if os.path.isfile(f)]

thedir = [f for f in os.listdir('/pylon2/bi4s86p/phuong/caenogastropod/17pdist/results/') if isfile(join('/pylon2/bi4s86p/phuong/caenogastropod/17pdist/results/', f))]

pdistdict = dict()

for thing in thedir:
	if '_AA.fasta.aligned.consensus.aliscore.NI.pdist' in thing and not thing in ignorelist:
		align(thing)





