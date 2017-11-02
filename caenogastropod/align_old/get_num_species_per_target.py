import os
import sys

thedir = [f for f in os.listdir('.') if os.path.isfile(f)]



splitdict = dict()

locusdict = dict()

species_num_loci = dict()

myconus = open('final_lottia_ref.fa', 'r')


for line in myconus:
	if ">" in line:

		mylottia = ''
		if '|' in line:
			item = line.strip().split('|')
			if len(item) > 6:
				mylottia = item[3]
			else:
				mylottia = item[2]
		else:
			mylottia = line.strip()[1:]
		locusdict[mylottia] = 0

for thing in thedir:
	if 'v2.fa' in thing:
		ID = thing.split('_')[0]

		myblast = open(thing, 'r')


		alreadyseen = []


		for line in myblast:
			if ">" in line:


				mylottia = ''
				if '|' in line:
					item = line.strip().split('|')
					if len(item) > 6:
						mylottia = item[-5]
					else:
						mylottia = item[2]
				else:
					mylottia = line.strip()[1:]




			if mylottia in alreadyseen:
				continue
			else:
				locusdict[mylottia] += 1
				alreadyseen.append(mylottia)



		species_num_loci[ID] = len(list(set(alreadyseen)))
		
		


out = open('num_species_per_target', 'w')

for thing in sorted(locusdict):
	out.write(thing + '\t' + str(locusdict[thing]) + '\n')

out.close()

out1 = open('num_targets_per_species' ,'w')

for item in species_num_loci:
	out1.write(item + '\t' + str(species_num_loci[item]) + '\n')

out1.close()







