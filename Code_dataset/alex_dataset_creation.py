import json
from pycocotools.coco import COCO
import skimage.io as io
import random
import csv

#madlibs = 'your/path/to/madlibs_train_v1/'
madlibs = 'madlibs_train_v1\\'
#coco_val_images = 'your/path/to/MSCOCO/images/val2014/'  # COCO validation images root
coco_val_images = 'madlibs_train_v1\\'
#coco_val_instances = 'your/path/to/MSCOCO/annotations/instances_val2014.json' # COCO validation instances file
coco_val_instances = 'annotations\instances_val2014.json'
#output file name
out_file = 'madlibs_dataset_out.csv'

# initialize COCO api
coco = COCO(coco_val_instances)

pair_relationships = json.load(open(madlibs+'tr_pair_relationships.json', 'r'))['tr_pair_relationships']
person_attributes = json.load(open(madlibs+'tr_person_attributes.json', 'r'))['tr_person_attributes']
object_attributes = json.load(open(madlibs+'tr_object_attributes.json', 'r'))['tr_object_attributes']
object_positions = json.load(open(madlibs+'tr_object_positions.json', 'r'))['tr_object_positions']


def getPersonAttributes(np, person_attributes, personID_pr):
    for pa in person_attributes:
        if len(pa['person_id_list']) == 1 and pa['person_id_list'][0] == personID_pr:
            attributeList = list(dict.fromkeys(pa['fitbs']))
            wearing = 0
            gender = 0
            genderList = ['man', 'woman', 'girl', 'boy']
            new_np=np
            for attribute in attributeList:
                firstWord = attribute.split(" ")[0]
                if (firstWord == 'wearing' or firstWord == 'dressed' or firstWord == 'in') and wearing < 1:
                    new_np = new_np + " " + attribute
                    wearing = wearing+1
                if gender<1:
                    if ("man" in attribute):
                        new_np = new_np.replace("person", "man")
                        gender = gender+1
                    elif ("woman" in attribute):
                        new_np = new_np.replace("person", "woman")
                        gender = gender+1
                    elif ("girl" in attribute):
                        new_np = new_np.replace("person", "girl")
                        gender = gender+1
                    elif ("boy" in attribute) and gender<1:
                        new_np = new_np.replace("person", "boy")
                        gender = gender+1

                if " " not in attribute and attribute not in genderList:
                    new_np = attribute + " " + new_np

            if new_np != np:
                return new_np
    return np

def getObjectAttributes(obj, object_attributes,objectID_pr):
    for oa in object_attributes:
        if len(oa['object_id_list']) == 1 and oa['object_id_list'][0] == objectID_pr:
            attributeList = list(dict.fromkeys(oa['fitbs']))
            new_obj=obj
            num_attr = 0
            for attribute in attributeList:
                firstWord = attribute.split(" ")[0]
                if (firstWord == 'in'):
                    new_obj = new_obj + " " + attribute

                elif " " not in attribute and num_attr<1:
                    new_obj = attribute + " " + new_obj
                    num_attr = num_attr+1

            if new_obj != obj:
                return new_obj
    return obj

def getObjectPosition(obj, object_positions,objectID_pr):
    for op in object_positions:
        if len(op['object_id_list']) == 1 and op['object_id_list'][0] == objectID_pr:
            positionList = list(dict.fromkeys(op['fitbs']))
            new_obj = obj
            position_added = 0
            for position in positionList:
                if " " in position and position_added < 1:
                    new_obj=obj + " " + position
                    position_added = position_added + 1
            if new_obj != obj:
                return new_obj
    return obj

with open(out_file, 'w') as csvfile:
    colNames = ['ImageID','LabelName1', 'LabelName2', 'ImageHeight', 'ImageWidth',
     'XMin1', 'XMax1', 'YMin1', 'YMax1','XMin2', 'XMax2', 'YMin2', 'YMax2','ReferringExpression']
    writer = csv.DictWriter(csvfile, delimiter=',', lineterminator='\n', fieldnames=colNames)
    writer.writeheader()
    count = 0
    pr_list = []
    for pr in pair_relationships:
        #get subject and object noun phrases
        #cut off last word of label text
        if len(pr['person_id_list']) == 1 and len(pr['object_id_list']) == 1:
            personID_pr = pr['person_id_list'][0]
            objectID_pr = pr['object_id_list'][0]

            LabelName1 = pr['prompt'][0].split(' ')[1]
            LabelName2 = pr['prompt'][1].rsplit('.', 1)[0]
            LabelName2 = LabelName2.split('the ')[1]

            image_id = pr['image_id']
            img_info = coco.loadImgs(image_id)
            person_id_list = pr['person_id_list']

            relationship = pr['fitbs'][0]

            np = LabelName1
            LabelName1 = getPersonAttributes(LabelName1, person_attributes, personID_pr)
            LabelName2 = getObjectAttributes(LabelName2, object_attributes, objectID_pr)
            LabelName2 = getObjectPosition(LabelName2, object_positions, objectID_pr)

            vre = "The " + LabelName1 + " is " + pr['fitbs'][0] + " the " + LabelName2 + "."

            #get coco annotation
            ann1 = coco.loadAnns(personID_pr)
            ann2 = coco.loadAnns(objectID_pr)

            img_height = img_info[0]['height']
            img_width = img_info[0]['width']

            #get bounding boxes, using actual pixel coordinates
            xMin1 = int(ann1[0]['bbox'][0])
            xMax1 = int(xMin1 + ann1[0]['bbox'][2])

            yMin1 = int(ann1[0]['bbox'][1])
            yMax1 = int(yMin1 + ann1[0]['bbox'][3])

            xMin2 = int(ann2[0]['bbox'][0])
            xMax2 = int(xMin2 + ann2[0]['bbox'][2])

            yMin2 = int(ann2[0]['bbox'][1])
            yMax2 = int(yMin2 + ann2[0]['bbox'][3])

            ImageID = 'alex_' + str(pr['image_id'])

            writer.writerow({'ImageID' : ImageID, 'LabelName1': LabelName1, 'LabelName2' : LabelName2, #'RelationshipLabel' : relationship,
                            'ImageHeight':img_height, 'ImageWidth': img_width, 'XMin1': xMin1, 'XMax1': xMax1, 'YMin1': yMin1, 'YMax1': yMax1,
                            'XMin2': xMin2, 'XMax2': xMax2, 'YMin2': yMin2, 'YMax2': yMax2,'ReferringExpression': vre})
            count = count + 1

    print('total annotations: ' + str(count))
