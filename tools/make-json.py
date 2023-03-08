from json import dump, load
import os, sys
fp = './in'

for file in os.listdir(fp):
	old_fp = f"{fp}/{file}"
	new_fp = f"./out/{file.replace('.txt', '.json')}"
	print(old_fp, new_fp)
	d = {
		"name":file.replace('.txt', ''),
		"lines": [
		]
	}
	with open(file) as txt:
		lines = txt.readlines()
		with open(new_fp, 'w') as json:
			for line in lines:
				iddd = line.split(':')[0]
				msss = line.split(':')[1]
				d['lines'].append({iddd: msss})
			dump(d, json)