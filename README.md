```md
<p align="center">
  <img src="https://i.imgur.com/mpu0yMQ.png" alt="Oil Spill Detection Banner" width="82%">
</p>

<h1 align="center">🛢️ Oil Spill Detection & Forensic Analysis</h1>

<p align="center">
AI-driven satellite spill detection • U-Net • DeepLabV3+ • AIS Integration • Streamlit Dashboard  
</p>

<br>

<!-- 🔥 CENTERED CUSTOM BADGES -->
<p align="center">

  <!-- Python -->
  <img src="https://img.shields.io/badge/Python-3.10%2B-2f77e5?style=for-the-badge&logo=python&logoColor=white"/>

  <!-- TensorFlow -->
  <img src="https://img.shields.io/badge/TensorFlow-2.16-fb8c00?style=for-the-badge&logo=tensorflow&logoColor=white"/>

  <!-- Models -->
  <img src="https://img.shields.io/badge/Models-U--Net%20%7C%20DeepLabV3%2B-43a047?style=for-the-badge&logo=keras&logoColor=white"/>

  <!-- Streamlit -->
  <img src="https://img.shields.io/badge/Streamlit-1.51-ff4b4b?style=for-the-badge&logo=streamlit&logoColor=white"/>

  <!-- OpenCV -->
  <img src="https://img.shields.io/badge/OpenCV-4.7-5c6bc0?style=for-the-badge&logo=opencv&logoColor=white"/>

  <!-- Status -->
  <img src="https://img.shields.io/badge/Status-Active-00c853?style=for-the-badge"/>

  <!-- License -->
  <img src="https://img.shields.io/badge/License-MIT-fdd835?style=for-the-badge"/>

</p>

<br>

---

# 📁 Project Structure

```

Oil_Spill_Project/
│
├── app.py                        # Streamlit Web Interface
│
├── data/
│   ├── train/                    # SAR images + masks (Kaggle)
│   ├── test/                     # SAR test images
│   └── ais_data/                 # AIS vessel-tracking CSV files
│
├── saved_models/                 # Trained .h5 model weights
│   ├── unet_oil_spill.h5
│   └── deeplabv3_oil_spill.h5
│
├── notebooks/
│   ├── 1_UNet_Training.ipynb
│   ├── 2_DeepLabV3_Training.ipynb
│   └── 3_Final_Inference.ipynb
│
├── 0_Prepare_AIS.py              # AIS data filter & cleaner
│
└── requirements.txt

```

---

# 📥 Required Datasets

## **1. Oil Spill Images (Satellite SAR Data)**  
**Source:**  
https://www.kaggle.com/competitions/airbus-ship-detection/data  

**Action:**  
Download → Unzip → Place files into:

```

data/train/
data/test/

```

---

## **2. AIS Vessel Data (Ship Tracking)**  
**Source:**  
https://marinecadastre.gov/ais/

**Action:**  
Download AIS CSV → Place into:

```

data/ais_data/

````

---

# 🚀 Features

### 🛰️ Oil Spill Segmentation  
Pixel-wise segmentation using **U-Net** and **DeepLabV3+**.

### 🔍 Forensic Visualization  
- Binary mask  
- Red spill overlay  
- Area calculation in km²  
- Confidence scoring  

### 🚢 AIS Vessel Tracking  
Identify and analyze vessels near spill location.

### 📊 Streamlit Dashboard  
Real-time inference, sliders, overlays, and severity levels.

### 🧠 Training Notebooks  
Contains full training-to-inference workflow.

---

# ⚙️ Installation

```bash
git clone https://github.com/YOUR_USERNAME/oil-spill-detection.git
cd oil-spill-detection

python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
````

---

# 🌐 Run the Web App

```bash
streamlit run app.py
```

---

# 🧠 Notebook Overview

| Notebook                     | Description                            |
| ---------------------------- | -------------------------------------- |
| `1_UNet_Training.ipynb`      | U-Net architecture + model training    |
| `2_DeepLabV3_Training.ipynb` | DeepLabV3+ segmentation experiments    |
| `3_Final_Inference.ipynb`    | Predictions, visualization, evaluation |

---

# 🛠 AIS Data Processing

```bash
python 0_Prepare_AIS.py
```

Generates:

```
vessel_data_clean.csv
```

---

# 🤝 How to Contribute (Fork → Clone → Branch → Commit → PR)

## **1️⃣ Fork**

[https://github.com/Spectrae/oil-spill-detection](https://github.com/Spectrae/oil-spill-detection)

## **2️⃣ Clone**

```bash
git clone https://github.com/YOUR-USERNAME/oil-spill-detection.git
cd oil-spill-detection
```

## **3️⃣ Branch**

```bash
git checkout -b feature-name
```

## **4️⃣ Commit**

```bash
git add .
git commit -m "Describe your changes"
```

## **5️⃣ Push**

```bash
git push origin feature-name
```

## **6️⃣ PR**

Open a Pull Request on GitHub.

---

# ⚠️ Do NOT Upload Large Files

❌ `data/train/`
❌ `data/test/`
❌ AIS CSV files
❌ `.jpg`, `.png`, `.tif`
❌ `.h5` model weights

These remain locally stored.

---

# 👨‍💻 Contributors

| Name              | Role                             | GitHub                                                     |
| ----------------- | -------------------------------- | ---------------------------------------------------------- |
| **Rick Mondal**   | Backend Developer                | [https://github.com/Spectrae](https://github.com/Spectrae) |
| **Contributor 2** | Model Research / Optimization    | *(Add link)*                                               |
| **Contributor 3** | AIS Data Cleaning / Processing   | *(Add link)*                                               |
| **Contributor 4** | Frontend Testing / Documentation | *(Add link)*                                               |

> Add more contributors as the project grows.

---

# 🔐 Security

See **SECURITY.md** for responsible vulnerability disclosures.

---

# 🛡️ License

Distributed under the **MIT License**.

---

<p align="center">
  <b>🌊 Advancing Environmental AI • One Pixel at a Time</b>
</p>

<br>

<p align="center">
  <b>❤️ Thank You!</b><br>
  Your contributions help make this project better for the community, researchers, and environmental applications worldwide.
</p>


