# Natural-Language-Processing
This is the project repo for NLP course 2020 fall. Project topic: Robot Scene Understanding using Referring Relationship

Dataset:
The dataset has 14 columns and the fieldnames = ['ImageID', 'LabelName1', 'LabelName2','Height', 'Width', 
'XMin1','XMax1', 'YMin1', 'YMax1', 'XMin2', 'XMax2', 'YMin2', 'YMax2', 'ReferringExpression']

where annotated the bounding boxes and the relationship between two objects in the image.
The synthetic dataset is created by using 3 different datasets with image/text augmentation.

1. Visual 7W (QA + BB -> VRE) -[Xiao Liu & Zijie]
   dataset address: http://ai.stanford.edu/~yukez/visual7w/
   - Xiao:
   This dataset is a Q&A dataset with bounding boxes included. The text augmentation is done by combining the 
   answer and the question, which resulted in a statement of the relationship between two objects in the image.
   QA pairs with only 2 objects involved are selected for our dataset creation. Xiao worked on combining "what" questions.
   code-> https://github.com/liuxiao1468/Natural-Language-Processing/blob/main/Code_dataset/Xiao_prep_data.py
   - Zijie:
2. Visual Genome - [Ziming]
   - Ziming:
3. Visual Madlibs - [Alex]
   - Alex:
