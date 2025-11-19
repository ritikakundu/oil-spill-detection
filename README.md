````markdown
<div align="center">

  <img src="https://i.imgur.com/mpu0yMQ.png" alt="Oil Spill Detection Banner" width="100%" style="border-radius: 10px;">

  <br />

  # 🛢️ Oil Spill Detection & Forensic Analysis

  **AI-Driven Satellite Imagery Segmentation & Vessel Tracking System**

  <p>
    <a href="#-features">Features</a> •
    <a href="#-installation">Installation</a> •
    <a href="#-usage">Usage</a> •
    <a href="#-dataset">Dataset</a> •
    <a href="#-tech-stack">Tech Stack</a>
  </p>

  <p>
    <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
    <img src="https://img.shields.io/badge/TensorFlow-2.16-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white" alt="TensorFlow">
    <img src="https://img.shields.io/badge/Keras-D00000?style=for-the-badge&logo=keras&logoColor=white" alt="Keras">
    <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit">
    <img src="https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white" alt="OpenCV">
    <br />
    <img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge" alt="Status">
    <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" alt="License">
  </p>

</div>

<br />

---

## 📖 Overview

The **Oil Spill Detection & Forensic Analysis** project leverages deep learning to automatically detect and map oil spills in satellite Synthetic Aperture Radar (SAR) imagery. By integrating **U-Net** and **DeepLabV3+** architectures, the system provides pixel-wise segmentation of affected areas.

Beyond detection, the platform incorporates **AIS (Automatic Identification System)** data to correlate spill locations with nearby vessel traffic, aiding in forensic analysis and potential source identification.

## ✨ Features

- **🛰️ Advanced Segmentation**: Utilizes U-Net and DeepLabV3+ for high-precision pixel-wise oil spill detection.
- **🔍 Forensic Analysis**: accurately calculates spill area (km²), overlays binary masks, and provides confidence scoring.
- **🚢 AIS Integration**: Correlates spill events with real-time vessel tracking data to identify potential sources.
- **📊 Interactive Dashboard**: A user-friendly **Streamlit** web interface for real-time inference and visualization.
- **📉 Comprehensive Notebooks**: Full training pipelines from data preprocessing to model evaluation.

---

## 📂 Project Structure

```bash
Oil_Spill_Project/
├── app.py                  # Main Streamlit Web Application
├── 0_Prepare_AIS.py        # AIS Data Cleaning & Preprocessing Script
├── requirements.txt        # Python Dependencies
│
├── data/                   # Dataset Directory (GitIgnored)
│   ├── train/              # Training SAR images + masks
│   ├── test/               # Test SAR images
│   └── ais_data/           # AIS vessel-tracking CSV files
│
├── saved_models/           # Pre-trained Model Weights
│   ├── unet_oil_spill.h5
│   └── deeplabv3_oil_spill.h5
│
└── notebooks/              # Jupyter Notebooks for Research
    ├── 1_UNet_Training.ipynb
    ├── 2_DeepLabV3_Training.ipynb
    └── 3_Final_Inference.ipynb
````

-----

## 🛠️ Installation

### 1\. Clone the Repository

```bash
git clone [https://github.com/Spectrae/oil-spill-detection.git](https://github.com/Spectrae/oil-spill-detection.git)
cd oil-spill-detection
```

### 2\. Set Up Virtual Environment

It is recommended to use a virtual environment to manage dependencies.

```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
```

### 3\. Install Dependencies

```bash
pip install -r requirements.txt
```

-----

## 💾 Dataset Setup

To train the models or run the app locally, you must download the datasets manually as they are too large for GitHub.

### 1\. Satellite SAR Imagery

  * **Source**: [Kaggle Airbus Ship Detection Challenge](https://www.kaggle.com/competitions/airbus-ship-detection/data)
  * **Instructions**: Download and unzip the data. Place training images and masks into `data/train/` and test images into `data/test/`.

### 2\. AIS Vessel Data

  * **Source**: [Marine Cadastre AIS Data](https://marinecadastre.gov/ais/)
  * **Instructions**: Download relevant AIS CSV files and place them into `data/ais_data/`.

-----

## 🚀 Usage

### Run the Web Dashboard

Launch the interactive Streamlit application to visualize predictions and analyze data.

```bash
streamlit run app.py
```

### Process AIS Data

Clean and filter raw AIS data for analysis.

```bash
python 0_Prepare_AIS.py
```

*Output: `vessel_data_clean.csv`*

### Training & Experimentation

Navigate to the `notebooks/` directory to explore the training logic.

  * **`1_UNet_Training.ipynb`**: Train the U-Net model.
  * **`2_DeepLabV3_Training.ipynb`**: Train the DeepLabV3+ model.
  * **`3_Final_Inference.ipynb`**: Run evaluation and visualize results.

-----

## 🤝 Contributing

Contributions are welcome\! Please follow these steps to contribute:

1.  **Fork** the repository.
2.  **Clone** your fork locally.
3.  **Create a Branch** (`git checkout -b feature/AmazingFeature`).
4.  **Commit** your changes (`git commit -m 'Add some AmazingFeature'`).
5.  **Push** to the branch (`git push origin feature/AmazingFeature`).
6.  **Open a Pull Request**.

> **Note**: Do not upload large dataset files (images, .h5 weights, or CSVs) to the repository.

-----

## 🛡️ License

This project is distributed under the **MIT License**. See `LICENSE` for more information.

-----

\<div align="center"\>

**🌊 Advancing Environmental Protection with AI** *Built with ❤️ by [Spectrae](https://github.com/Spectrae)*

\</div\>

```
```