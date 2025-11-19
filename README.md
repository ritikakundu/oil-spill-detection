# Oil Spill Detection Using Deep Learning

A complete pipeline for **oil spill segmentation** using **U-Net** and **DeepLabV3+**, trained on satellite imagery and enhanced with **AIS (Automatic Identification System) marine traffic data**.

This project includes training notebooks, an inference pipeline, and a clean structure to help teams collaborate efficiently.

---

## Project Structure

```plaintext
Oil_Spill_Project/
├── data/
│   ├── train/               # Kaggle Train dataset (images + masks)
│   ├── test/                # Kaggle Test dataset
│   └── ais_data/            # Marine Cadastre AIS ship-tracking data
│
├── saved_models/            # Trained model weights (.h5 files) are saved here
│
├── notebooks/
│   ├── 1_UNet_Training.ipynb        # U-Net architecture training workflow
│   ├── 2_DeepLabV3_Training.ipynb   # DeepLabV3+ model training notebook
│   └── 3_Final_Inference.ipynb      # Inference pipeline + evaluation
│
└── requirements.txt         # Python dependencies for the project
