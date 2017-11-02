#!/usr/bin/env python


import os
import sys
import argparse
import multiprocessing



thedir = [f for f in os.listdir('.') if os.path.isfile(f)]



for thing in thedir:
	if 'transcriptfasta' in thing:
		mylist.append(thing)

		cmd = 'java -jar /home/phuong/macse_v1.2.jar -prog alignSequences -seq ' + thing
		os.system(cmd)
