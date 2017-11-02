import os
import sys

filelist = ['pfover50', 'pfadnan', 'pfall']

counter = 0

for thing in ['greater_than_50', 'adnan_only', 'all_files']:
	out = open('partition_finder.cfg', 'w')




	variables = dict(
	sample = thing
	) #name your output


	commands = """## ALIGNMENT FILE ##
alignment = {sample}.phy;

## BRANCHLENGTHS: linked | unlinked ##
branchlengths = linked;

## MODELS OF EVOLUTION for PartitionFinder: all | raxml | mrbayes | <list> ##
##              for PartitionFinderProtein: all_protein | <list> ##
models = all_protein;

# MODEL SELECCTION: AIC | AICc | BIC #
model_selection = BIC;


## DATA BLOCKS: see manual for how to define ##
[data_blocks]
""".format(**variables)

	out.write(commands)
	mynexus = open(thing + '.nexus', 'r')

	for line in mynexus:
		if 'charset' in line:
			out.write(line.replace('charset ', '').replace('.nexus',''))


	commands = """
## SCHEMES, search: all | user | greedy ##
[schemes]
search = hcluster;

#user schemes go here if search=user. See manual for how to define.#""".format(**variables)

	out.write(commands)
	out.close()

	os.system('mv partition_finder.cfg ' + filelist[counter])
	os.system('cp ' + thing + '.phy ' + filelist[counter] + '/')
	counter += 1

