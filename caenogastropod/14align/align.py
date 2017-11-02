import os
import sys



adnan = open('adnan_loci', 'r')

adnanlist = []

for line in adnan:
	adnanlist.append(line.strip())

print adnanlist


thedir = [f for f in os.listdir('.') if os.path.isfile(f)]


for thing in thedir:
	if 'AA.fasta' in thing:


		myfasta = open(thing, 'r')

		ID = thing.split('_')[0]

		nameslist = []

		for line in myfasta:
			if ">" in line:
				name = line.strip().split('|')[0][1:]

				if name in nameslist:
					continue
				else:
					nameslist.append(name)

		if ID in adnanlist or len(nameslist) > 42:

			cmd = '/home/phuong/mafft/bin/mafft ' + thing + ' > ' + thing + '.aligned'
			os.system(cmd)
			cmd = 'cp ' + thing + '.aligned /pylon2/bi4s86p/phuong/caenogastropod/14align/aligned'
			os.system(cmd)

		else:
			continue




















