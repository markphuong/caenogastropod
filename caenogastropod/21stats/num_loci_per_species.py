import os
import sys
from os.path import isfile, join

thedir = [f for f in os.listdir('/pylon2/bi4s86p/phuong/caenogastropod/20treebuilding/keptfastas/') if isfile(join('/pylon2/bi4s86p/phuong/caenogastropod/20treebuilding/keptfastas/', f))]



adnanlist = []

adnan = open('adnan_loci', 'r')

for line in adnan:
        adnanlist.append(line.strip())


speciesdictadnan = dict()
locidictadnan = dict()


speciesdict = dict()
locidict  = dict()

for thing in thedir:
	if '.pdist' in thing:
		myfasta = open(thing, 'r')

		locus = thing.split('_')[0]

		locidict[locus] = 0

		for line in myfasta:
			if ">" in line:
				speciesname =line.strip()[1:]

				locidict[locus] += 1

				if speciesname in speciesdict:
					speciesdict[speciesname] += 1
				else:
					speciesdict[speciesname] = 1
	                        if locus in adnanlist:
        	                        if locus in locidictadnan:
                	                        locidictadnan[locus] += 1
                        	        else:
                                	        locidictadnan[locus] = 1

                                	if speciesname in speciesdictadnan:
                                	        speciesdictadnan[speciesname] += 1
                                	else:
                                        	speciesdictadnan[speciesname] = 1



out = open('num_species_per_target', 'w')

for item in locidict:
	out.write(item + '\t' + str(locidict[item]) + '\n')

out.close()

out = open('num_target_per_species', 'w')

for item in speciesdict:
	out.write(item + '\t' + str(speciesdict[item]) + '\n')

out = open('num_species_per_target_adnan', 'w')

for item in locidictadnan:
        out.write(item + '\t' + str(locidictadnan[item]) + '\n')

out.close()

out = open('num_target_per_species_adnan', 'w')

for item in speciesdictadnan:
        out.write(item + '\t' + str(speciesdictadnan[item]) + '\n')



