from json import load, dump
from os import listdir

for txtfile in listdir('./inputs/'):
	data = [

	]
	with open('./inputs/' + txtfile) as f:
		lines = f.readlines()
		for line in lines:
			l_split = line.rstrip().split(':')
			if len(l_split) == 1:
				data.append({
					"": line
				})
			else: 
				data.append({
					l_split[0]: l_split[1]
				})
	with open('./outputs/' + txtfile.replace('.txt', '.json'), 'x') as jsonfile:
		dump(data, jsonfile, indent=4)