# ViLBERT (Modified)

Code and pre-trained models for **[ViLBERT: Pretraining Task-Agnostic VisiolinguisticRepresentations for Vision-and-Language Tasks](https://arxiv.org/abs/1908.02265)**.

<span style="color:blue"> *Note: This codebase is still in beta release to replicate the paper's preformance. * </span>

## Repository Setup

1. Create a fresh conda environment, and install all dependencies.

```text
conda create -n vilbert python=3.6
conda activate vilbert
git clone https://github.com/jiasenlu/vilbert_beta
cd vilbert_beta
pip install -r requirements.txt
```

2. Install pytorch
```
conda install pytorch torchvision cudatoolkit=10.0 -c pytorch
```

3. Install apx, follows https://github.com/NVIDIA/apex

4. compile tools

```
cd tools/refer
make
```
## Data Setup

Check `README.md` under `data` for more details.  Check  `vlbert_tasks.yml` for more details. 


## Pre-trained model for Evaluation

| Model | Objective | Link |
|:-------:|:------:|:------:|

|ViLBERT 6-Layer| RefCOCO+ |[Google Drive](https://drive.google.com/drive/folders/1GWY2fEbZCYHkcnxd0oysU0olfPdzcD3l?usp=sharing)|


## Evaluation


### RefCOCO+

1: Download the pretrained model with objective `RefCOCO+` and put it under `save`

2: We use the Pre-computed detections/masks from [MAttNet](https://github.com/lichengunc/MAttNet) for fully-automatic comprehension task, Check the MAttNet repository for more details. 

3: To test on the RefCOCO+ val set and use the following command:

```bash
python eval_tasks.py --bert_model bert-base-uncased --from_pretrained save/refcoco+_bert_base_6layer_6conect-pretrained/pytorch_model_19.bin --config_file config/bert_base_6layer_6conect.json --task 4
```

### Train ViLBERT for DownStream Tasks

### Refer Expression

```bash
python train_tasks.py --bert_model bert-base-uncased --from_pretrained save/refcoco+_bert_base_6layer_6conect-pretrained/pytorch_model_19.bin --config_file config/bert_base_6layer_6conect.json  --learning_rate 4e-5 --num_workers 16 --tasks 4 --save_name pretrained
```

- For single GPU training, use smaller batch size and simply remove ` -m torch.distributed.launch --nproc_per_node=8 --nnodes=1 --node_rank=0 ` 

## References

If you find this code is useful for your research, please cite the paper

```
@article{lu2019vilbert,
  title={ViLBERT: Pretraining Task-Agnostic Visiolinguistic Representations for Vision-and-Language Tasks},
  author={Lu, Jiasen and Batra, Dhruv and Parikh, Devi and Lee, Stefan},
  journal={arXiv preprint arXiv:1908.02265},
  year={2019}
}
```

