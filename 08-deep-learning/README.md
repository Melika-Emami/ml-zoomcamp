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

- **Baseline (10 epochs).** Resize images to `200 × 200`, apply ImageNet normalization, and train with `BCEWithLogitsLoss`. Metrics are saved to `history_baseline.json`.
- **Augmentation (10 additional epochs).** Continue training the baseline model with random rotations up to 50°, random resized crops, and horizontal flips on the training images. Metrics for these 10 epochs are saved to `history_augmented.json`.

Both phases record training and held-out loss and accuracy after each epoch. The held-out images use the baseline transform throughout.