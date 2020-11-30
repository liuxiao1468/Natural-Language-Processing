# ViLBERT <img src="fig/vilbert_trim.png" width="45">

#### ViLBERT_beta has been deprecated. Please see [vilbert-multi-task](https://github.com/facebookresearch/vilbert-multi-task), which includes implementations for [12-in-1: Multi-Task Vision and Language Representation Learning](https://arxiv.org/abs/1912.02315)

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
|ViLBERT 2-Layer| Conceptual Caption |[Google Drive](https://drive.google.com/drive/folders/1asaQDYTacetm12j1K4AkYWdjPincLnap?usp=sharing)|
|ViLBERT 4-Layer| Conceptual Caption |[Google Drive](https://drive.google.com/drive/folders/1uDa1UsJC-Vz0ZdbHUMw5imRGhk5oM-YR?usp=sharing)|
|ViLBERT 6-Layer| Conceptual Caption |[Google Drive](https://drive.google.com/drive/folders/1JVM5WiolJJLnY9_lruxSaSop7IFX8a-v?usp=sharing)|
|ViLBERT 8-Layer| Conceptual Caption |[Google Drive](https://drive.google.com/drive/folders/1M-QoxLB6WJaqY9nq4KzPwfpJ8Va5FNCy?usp=sharing)|
|ViLBERT 6-Layer| VQA |[Google Drive](https://drive.google.com/drive/folders/1nrcVww0u_vozcFRQVr58-YH5LOU1ZiWT?usp=sharing)|
|ViLBERT 6-Layer| VCR |[Google Drive](https://drive.google.com/drive/folders/1QJuMzBarTKU_hAWDSZm60rWiDnbAVEVZ?usp=sharing)|
|ViLBERT 6-Layer| RefCOCO+ |[Google Drive](https://drive.google.com/drive/folders/1GWY2fEbZCYHkcnxd0oysU0olfPdzcD3l?usp=sharing)|
|ViLBERT 6-Layer| Image Retrieval |[Google Drive](https://drive.google.com/drive/folders/18zUTF3ZyOEuOT1z1aykwtIkBUhfROmJo?usp=sharing)|

## Evaluation


### RefCOCO+

1: Download the pretrained model with objective `RefCOCO+` and put it under `save`

2: We use the Pre-computed detections/masks from [MAttNet](https://github.com/lichengunc/MAttNet) for fully-automatic comprehension task, Check the MAttNet repository for more details. 

3: To test on the RefCOCO+ val set and use the following command:

```bash
python eval_tasks.py --bert_model bert-base-uncased --from_pretrained save/refcoco+_bert_base_6layer_6conect-pretrained/pytorch_model_19.bin --config_file config/bert_base_6layer_6conect.json --task 4
```

## Visiolinguistic Pre-training

Once you extracted all the image features, to train a 6-layer ViLBERT model on conceptual caption:

```bash
python -m torch.distributed.launch --nproc_per_node=8 --nnodes=1 --node_rank=0 train_concap.py --from_pretrained bert-base-uncased --bert_model bert-base-uncased --conf
ig_file config/bert_base_6layer_6conect.json --learning_rate 1e-4 --train_batch_size 512 --save_name pretrained
```

### Train ViLBERT for DownStream Tasks



### Refer Expression

```bash
python -m torch.distributed.launch --nproc_per_node=8 --nnodes=1 --node_rank=0 train_tasks.py --bert_model bert-base-uncased --from_pretrained save/bert_base_6_layer_6_connect_freeze_0/pytorch_model_8.bin  --config_file config/bert_base_6layer_6conect.json  --learning_rate 4e-5 --num_workers 16 --tasks 4 --save_name pretrained
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



## Why does ViLBERT look like <img src="fig/vilbert_trim.png" width="45">? 

<p align="center">
<img src="fig/vilbert.png" width="400" >
</p>
