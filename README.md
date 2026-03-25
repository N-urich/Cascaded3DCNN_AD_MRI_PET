# Cascaded3DCNN_AD_MRI_PET
Cascaded 3D-CNN with Progressive Multimodal Fusion for Alzheimer's Disease Classification using MRI and PET
# Cascaded 3D-CNN with Progressive Multimodal Fusion
## For Alzheimer's Disease Classification using MRI and PET

This is the official implementation of the paper submitted to IAAST International Conference.

## Abstract
Single-modal neuroimaging approaches for Alzheimer's disease diagnosis remain limited.
We propose a cascaded 3D-CNN that fuses structural MRI and metabolic PET images
with progressive confidence-aware fusion.

## Model Architecture
![model](figures/model_architecture.png)

## Main Results
- AD vs NC: 98.25% Accuracy
- AD vs MCI: 93.75% Accuracy
- MCI vs NC: 89.30% Accuracy
- AUC: 99.15%

## Requirements
torch>=2.0.0
numpy
SimpleITK
nibabel

## How to Run
1. Install requirements
2. Prepare ADNI dataset
3. Run training: python train.py
4. Evaluate: python test.py

## Dataset
ADNI database: https://adni.loni.usc.edu/

## Citation
If you use this code, please cite our paper.
