import csv

my_dict = {}
my_other_dict = {}

with open('Census_by_Community_2018.csv','r') as csvFile:
	reader = csv.DictReader(csvFile)
	counter = 0
	for row in reader:
		counter += 1
		key = row['CLASS']
		key2 = row['SECTOR']
		value = int(row['RES_CNT'])
		if key in my_dict.keys():
			my_dict[key] += value
		else:
			my_dict[key] = value
		if key2 in my_other_dict.keys():
			my_other_dict[key2] += value
		else:
			my_other_dict[key2] = value
	print(my_dict)
	print(my_other_dict)
	print('Number of lines', counter)

with open("report.txt", "w") as f:
	f.write('---------------- \n')
	f.write('CLASS SUMMARY \n')
	f.write('---------------- \n')
	for k, v in my_dict.items():
			f.write(f'{k}:{v}')
			f.write('\n')
	f.write('---------------- \n')
	f.write('SECTOR SUMMARY \n')
	f.write('---------------- \n')
	for k, v in my_other_dict.items():
			f.write(f'{k}:{v}')
			f.write('\n')
	f.write('---------------- \n')		
	f.write(f'There are {counter} lines in the file')
	f.close()
