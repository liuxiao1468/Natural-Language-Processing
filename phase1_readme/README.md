# Natural-Language-Processing
This is the readme for phase1 submission. Project topic: Robot Scene Understanding using Referring Relationship

Model:

## 1. Vil-Bert model
   model address: https://github.com/jiasenlu/vilbert_beta
   - **Xiao & Ziming**:
   We used a conda env for installing the vil-Bert model and pytorch with other deeplearning packages:
```
conda create -n vilbert python=3.6
conda activate vilbert
git clone https://github.com/jiasenlu/vilbert_beta
cd vilbert_beta
pip install -r requirements.txt
conda install pytorch torchvision cudatoolkit=10.0 -c pytorch
cd tools/refer
make
```
For using a pretrained model with 6-Layer vil-Bert, simply go to https://drive.google.com/drive/folders/1GWY2fEbZCYHkcnxd0oysU0olfPdzcD3l and save the downloaded model under '~/vilbert_beta/save'. 



## 2. VL-Bert model
   model address: https://github.com/jackroos/VL-BERT
   - **Alex & Zijie**: 
