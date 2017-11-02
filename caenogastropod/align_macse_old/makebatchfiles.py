


counter = 0
while counter < 34:
	mybatch = open('align_batch', 'r')

	out = open('align_batch' + str(counter), 'w')

	for line in mybatch:
		if 'mapfile' in line:
			line = line.replace('mapfile_newref', 'mapfile' + str(counter))
			out.write(line)
		else:
			out.write(line)
	out.close()
	counter += 1