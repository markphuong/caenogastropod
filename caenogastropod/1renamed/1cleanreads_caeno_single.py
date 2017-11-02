#!/usr/bin/env python

#flash manual: http://ccb.jhu.edu/software/FLASH/MANUAL

#this script cleans reads using trimmomatic, merges reads using flash, and creates a read1 file, read2 file (these represent paired files) and an unpaired file

import os
import sys
import argparse
import multiprocessing


# an arguments portion in the code represents necessary inputs to give to the script. I usually use this to give the program a file that contains all the unique sample IDs which should be in the read file names
def get_args():
	parser = argparse.ArgumentParser(description="run blastx")


	required = parser.add_argument_group("required arguments") 
	required.add_argument("--map", help="textfile with samples to run and what fasta file to match it to", required=True) #A map file with the sample ID and the fasta file it goes to

	return parser.parse_args()


def align(element):


	#the adapters file should have both forward and reverse, and the universal adapters
	
	#this variables dict species the names for the input/out files
	variables = dict(
	adfile = 'adapters_caeno_7_8_2016.fa',
	read1 = element + '_unpaired.fastq',
	read1out = element + '_finalunpaired.fq',
	sampleID = element) #name your output


	commands = """
	java -jar $TRIMMOMATIC_HOME/trimmomatic-0.36.jar SE -threads 63 -phred33 {read1} {read1out} ILLUMINACLIP:{adfile}:2:40:15 SLIDINGWINDOW:4:20 MINLEN:36 LEADING:15 TRAILING:15 > {sampleID}.trimm 2> {sampleID}.trimmerr
	""".format(**variables)


	#this bit of code executes the command

	cmd_list = commands.split("\n")
	for cmd in cmd_list:
		os.system(cmd)

mylist = []


args = get_args() #this is where the arguments from the def args code gets called upon

with open(args.map) as rfile:
	for line in rfile:
		line = line.strip()
		# align(line)
		mylist.append(line)

#this bit is really not necessary. I could have done this by not having 'def main()' and just starting with the args=get_args() line, but the following code follows the logic of what preceded it.


pool = multiprocessing.Pool(2)
pool.map(align, mylist)






