from ete3 import Tree
import os
import sys


thedir = [f for f in os.listdir('.') if os.path.isfile(f)]


out = open('failed_tree_filter', 'w')

for thing in thedir:
	if '_AA.fasta.aligned.consensus.aliscore.NI' in thing:
		
		treefile = thing.split('_')[0] + '_fasttree.tre'

		cmd = './FastTree -wag ' + thing + ' > ' + treefile
		os.system(cmd)

		t = Tree(treefile)

		myleaves = []

		for leaf in t:
			myleaves.append(leaf.name)

		if 'jgi' in myleaves:
			t.set_outgroup ( t&"jgi" )
		elif 'PATELLO-Nacellidae-Cellana-tramoserica' in myleaves:
			t.set_outgroup ( t&"PATELLO-Nacellidae-Cellana-tramoserica" )
		elif 'PATELLO-Lottiidae-Cellana-tramosevica' in myleaves:
			t.set_outgroup ( t&"PATELLO-Lottiidae-Cellana-tramosevica" )
		else:
			l = [myleaves.index(i) for i in myleaves if 'VETI-' in i]
			t.set_outgroup ( t&myleaves[l[0]] )
			


		leaves = []
		leaves2 = []

		for leaf in t:
			if 'HETERO' in leaf.name:
				leaves2.append(leaf.name)
			elif 'CAENO' in leaf.name:
				if 'CAENO-Litiopidae-Phasianella-ventricosa' in leaf.name:
					continue
				elif 'CAENO-Turridae-Vexitomina-garrardi' in leaf.name:
					leaves2.append(leaf.name)
				else:
					leaves.append(leaf.name)
					leaves2.append(leaf.name)


#			if 'VETI' in leaf.name or 'CAENO-Litiopidae-Phasianella-ventricosa' in leaf.name:
#				leaves.append(leaf.name)
#			else:
#				continue

				#if 'CAENO-Turridae-Vexitomina-garrardi' in leaf.name or 'CAENO-Litiopidae-Phasianella-ventricosa' in leaf.name:
				#	continue
				#else:
				#	leaves.append(leaf.name)


		if t.check_monophyly(values=leaves, target_attr="name")[1] == 'monophyletic' or t.check_monophyly(values=leaves2, target_attr="name")[1] == 'monophyletic':
			continue
		else:
			out.write(thing + '\n')
