#http://biopython.org/wiki/AlignIO

#!/usr/bin/env python

from Bio import SeqIO

import os
import sys
from collections import defaultdict
from pprint import pprint
import argparse
import multiprocessing
from Bio.Alphabet import generic_dna, Gapped, generic_protein
from Bio import AlignIO

alignment = AlignIO.read(open(sys.argv[1]), 'nexus',alphabet=Gapped(generic_protein))

output = open(sys.argv[2], 'w')

AlignIO.write(alignment, output, "phylip-sequential")
