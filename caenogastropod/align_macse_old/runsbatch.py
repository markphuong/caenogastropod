import os
import sys


counter = 0
while counter < 34:

	cmd = 'sbatch align_batch' + str(counter)

	os.system(cmd)
	counter += 1
