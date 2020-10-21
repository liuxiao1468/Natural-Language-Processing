import numpy as np
import cv2
import csv
import random
import itertools
import json

data_A = []
data_B = []
data_C = []
data_D = []

with open(r'Alex_dataset.csv','rt')as f:
	data = csv.reader(f)
	for row in data:
		data_A.append(row)

data_A = data_A[1:2001]

with open(r'dataset_prep_xiao.csv','rt')as f:
	data = csv.reader(f)
	for row in data:
		data_B.append(row)

data_B = data_B[1:2001]

with open(r'dataset_prep_Zijie.csv','rt')as f:
	data = csv.reader(f)
	for row in data:
		data_C.append(row)

data_C = data_C[1:2001]

with open(r'Ziming_dataset.csv','rt')as f:
	data = csv.reader(f)
	for row in data:
		data_D.append(row)

data_D = data_D[1:2001]


with open('dataset.csv', mode='w') as csv_file:
	fieldnames = ['ImageID', 'LabelName1', 'LabelName2','Height', 'Width', 'XMin1','XMax1', 'YMin1', 'YMax1', 'XMin2', 'XMax2', 'YMin2', 'YMax2', 'ReferringExpression']
	writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
	writer.writeheader()
	for i in range (len(data_A)):
		string = data_A[i]
		writer.writerow({'ImageID': string[0], 'LabelName1': string[1], 'LabelName2':string[2], 'Height':string[3],'Width': string[4],
						'XMin1':string[5], 'XMax1': string[6], 'YMin1': string[7],
						'YMax1':string[8], 'XMin2':string[9], 'XMax2':string[10],
						'YMin2':string[11], 'YMax2':string[12], 'ReferringExpression': string[13]})
	for i in range (len(data_B)):
		string = data_B[i]
		writer.writerow({'ImageID': string[0], 'LabelName1': string[1], 'LabelName2':string[2], 'Height':string[3],'Width': string[4],
						'XMin1':string[5], 'XMax1': string[6], 'YMin1': string[7],
						'YMax1':string[8], 'XMin2':string[9], 'XMax2':string[10],
						'YMin2':string[11], 'YMax2':string[12], 'ReferringExpression': string[13]})
	for i in range (len(data_C)):
		string = data_C[i]
		writer.writerow({'ImageID': string[0], 'LabelName1': string[1], 'LabelName2':string[2], 'Height':string[3],'Width': string[4],
						'XMin1':string[5], 'XMax1': string[6], 'YMin1': string[7],
						'YMax1':string[8], 'XMin2':string[9], 'XMax2':string[10],
						'YMin2':string[11], 'YMax2':string[12], 'ReferringExpression': string[13]})
	for i in range (len(data_D)):
		string = data_D[i]
		writer.writerow({'ImageID': string[0], 'LabelName1': string[1], 'LabelName2':string[2], 'Height':string[3],'Width': string[4],
						'XMin1':string[5], 'XMax1': string[6], 'YMin1': string[7],
						'YMax1':string[8], 'XMin2':string[9], 'XMax2':string[10],
						'YMin2':string[11], 'YMax2':string[12], 'ReferringExpression': string[13]})





