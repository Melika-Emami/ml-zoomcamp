# Straight vs Curly Hair Classification

A PyTorch CNN that classifies photos as curly or straight hair. This project is part of Machine Learning Zoomcamp Homework 8.

## Dataset

[Download `data.zip`](https://github.com/SVizor42/ML_Zoomcamp/releases/download/straight-curly-data/data.zip) and extract it in the project root. Use the supplied training and held-out evaluation splits.

Expected SHA-256: `9e53453e3017502f22860cb08558f0cdb343e102fb61feab75960616185e7d67`

## CPU setup

Use Python 3.11. From the project root, install the pinned dependencies in [`requirements-cpu.txt`](requirements-cpu.txt):

```bash
python -m pip install -r requirement.txt
```

Run training and evaluation on the CPU to reproduce the grading baseline.

## Training

The baseline resizes images to 200 × 200, applies ImageNet normalization, and trains for 10 epochs with `BCEWithLogitsLoss`. After each epoch, the model is evaluated on the held-out split. Training and evaluation loss and accuracy are saved to `history_baseline.json`.