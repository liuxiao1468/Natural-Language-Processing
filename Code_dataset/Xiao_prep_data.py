import numpy as np
import cv2
import csv
import random
import itertools
import json


with open('/home/leo/deeplearning/nlp/dataset_v7w_telling.json') as f:
    data = json.load(f)

with open('/home/leo/deeplearning/nlp/dataset_v7w_grounding_annotations/v7w_telling_answers.json') as f:
    boxes = json.load(f)

data_1 = data['images']
# print(len(data_1))
# print(len(data_1[0]['qa_pairs']))
# print(data_1[0]['qa_pairs'][0]['type'])

count = 0


def check(string):
	a = string.split()
	if (a[1] == 'is') or (a[1] == 'are'):
		return True
	else:
		return False


def combine_qa(a, b):
	a = a.replace('?', '')
	b = b.replace('.', '')
	a = a.split()
	a.pop(0)
	a.insert(0, b)
	str1 = ' '.join([str(elem) for elem in a])
	return str1


with open('dataset_prep.csv', mode='w') as csv_file:
	fieldnames = ['ImageID', 'LabelName1', 'LabelName2','Height', 'Width', 'XMin1','XMax1', 'YMin1', 'YMax1', 'XMin2', 'XMax2', 'YMin2', 'YMax2', 'ReferringExpression']
	writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
	writer.writeheader()
	i = 0
	while (count<=2000) and (i< len(data_1)):
		sample = data['images'][i]
		i = i+1
		for j in range(len(sample['qa_pairs'])):
			if sample['qa_pairs'][j]['type'] == 'what':
				# print(sample['qa_pairs'][j]['qa_id'], sample['qa_pairs'][j]['type']
				# 	, "ImageID: ", sample['qa_pairs'][j]['image_id'])
				temp = 0
				string = []
				for k in range(len(boxes['boxes'])):
					if boxes['boxes'][k]['qa_id'] == sample['qa_pairs'][j]['qa_id']:
						temp = temp+1
						string.append(boxes['boxes'][k]['name'])
						string.append(boxes['boxes'][k]['height'])
						string.append(boxes['boxes'][k]['width'])
						string.append(boxes['boxes'][k]['y'])
						string.append(boxes['boxes'][k]['x'])
				if temp == 2:
					aa = check(sample['qa_pairs'][j]['question'])
					if aa == True:
						count = count+1
						string.append(sample['qa_pairs'][j]['image_id'])
						string.append(sample['qa_pairs'][j]['question'])
						string.append(sample['qa_pairs'][j]['answer'])
						# print(string)
						expression = combine_qa(string[11],string[12])
						path = '/home/leo/deeplearning/nlp/visual7w_images/images/v7w_'+str(sample['qa_pairs'][j]['image_id'])+'.jpg'
						img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

						writer.writerow({'ImageID': string[10], 'LabelName1': string[0], 'LabelName2':string[5], 'Height':img.shape[0],'Width': img.shape[1],
						'XMin1':string[4], 'XMax1': string[4]+string[2], 'YMin1': string[3],
						'YMax1':string[3]+string[1], 'XMin2':string[9], 'XMax2':string[9]+string[7],
						'YMin2':string[8], 'YMax2':string[8]+string[6], 'ReferringExpression': expression })
					# break
		print(count)
	print("useful:", count)

















