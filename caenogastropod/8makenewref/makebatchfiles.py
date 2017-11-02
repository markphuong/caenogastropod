


counter = 0
while counter < 17:
	mybatch = open('newrefbatch', 'r')

	out = open('newrefbatch' + str(counter), 'w')

	for line in mybatch:
		if 'mapfile' in line:
			line = line.replace('mapfile_newref', 'mapfile' + str(counter))
			out.write(line)
		else:
			out.write(line)
	out.close()
	counter += 1