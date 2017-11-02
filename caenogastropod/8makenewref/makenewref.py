import os
import sys
from collections import defaultdict
import multiprocessing
from os import listdir
from os.path import isfile, join
import argparse



def get_args(): #arguments needed to give to this script
        parser = argparse.ArgumentParser(description="run novoalign")

        #forces required argument to let it run
        required = parser.add_argument_group("required arguments")
        required.add_argument("--map", help="textfile with samples to run and what fasta file to match it to", required=True) #A map file with the sample ID and the fasta file it goes to

        return parser.parse_args()



def align(element):

	ID = element.split('.')[0]

	lottiadict = dict()

	mylottia = open('Lotgi1_GeneModels_FilteredModels1_aa.fasta.NI', 'r')

	for line in mylottia:
		if ">" in line:
			name = line.strip().split('|')[2]
			seq = next(mylottia).strip()

			lottiadict[name] = seq


	out = open(ID +'.lotgi.fasta', 'w')
	out.write('>' + ID + '\n')
	out.write(lottiadict[ID] + '\n')
	out.close()

	variables = dict(
	sample = ID
	) #name your output


	commands = """
	cp /pylon2/bi4s86p/phuong/caenogastropod/7separatefasta/fasta/{sample}.fasta ./
	makeblastdb -dbtype prot -in {sample}.lotgi.fasta
	/home/phuong/TransDecoder-3.0.0/TransDecoder.LongOrfs -t {sample}.fasta
	/home/phuong/TransDecoder-3.0.0/TransDecoder.Predict -t {sample}.fasta
	python makesomethingNotInterleaved.py {sample}.fasta.transdecoder.pep {sample}.fasta.transdecoder.pep.NI
	python refine_headers.py {sample}.fasta.transdecoder.pep.NI {sample}.fasta.transdecoder.pep.NI.refined
	blastp -query {sample}.fasta.transdecoder.pep.NI.refined -db {sample}.lotgi.fasta -outfmt 6 -out {sample}.mytempblast -evalue 1e-10
	python parse_blast_to_make_new_reference.py {sample}.lotgi.fasta {sample}.mytempblast {sample}.fasta.transdecoder.pep.NI.refined {sample}.mynewref.fa
	cp {sample}.mynewref.fa /pylon2/bi4s86p/phuong/caenogastropod/8makenewref/newrefs_16/
	cp {sample}.mytempblast /pylon2/bi4s86p/phuong/caenogastropod/8makenewref/newrefs_16/
	rm -r {sample}*
	""".format(**variables)



	cmd_list = commands.split("\n")
	for cmd in cmd_list:
		os.system(cmd)

mylist = []


args = get_args()

        #Make a list of lists, each list within the list will have the first and second elements of the map file that are separated by a tab

with open(args.map) as rfile:
        for line in rfile:
                line = line.strip()
 #               mylist.append(line)
		align(line)


#pool = multiprocessing.Pool(62)
#pool.map(align, mylist)#run the function with the arguments

















