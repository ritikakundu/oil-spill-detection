import streamlit as st
import numpy as np
import cv2
import tensorflow as tf
from tensorflow.keras.models import load_model

# --- CONFIGURATION ---
st.set_page_config(page_title="Oil Spill Forensic Tool", page_icon="🛢️", layout="wide")

# --- SIDEBAR ---
st.sidebar.title("🔧 Control Panel")
confidence_threshold = st.sidebar.slider("Detection Sensitivity", 0.0, 1.0, 0.05, 0.01)
st.sidebar.info("Lower sensitivity detects fainter spills. Higher sensitivity reduces false alarms.")

# --- MAIN APP ---
st.title("🛢️ Oil Spill Forensic System")
st.markdown("Upload a Satellite SAR image to detect oil spills and assess environmental damage.")

# Load Model (Cached so it doesn't reload every time)
@st.cache_resource
def load_ai_model():
    return load_model('saved_models/unet_oil_spill.h5')

try:
    model = load_ai_model()
    st.sidebar.success("AI Model Loaded Successfully")
except Exception as e:
    st.error(f"Error loading model: {e}")

uploaded_file = st.file_uploader("Choose a Satellite Image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # 1. Read Image
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    original_img = cv2.imdecode(file_bytes, 1)
    original_img = cv2.cvtColor(original_img, cv2.COLOR_BGR2RGB)
    
    # 2. Preprocess
    img_resized = cv2.resize(original_img, (256, 256))
    input_data = np.expand_dims(img_resized, axis=0) / 255.0
    
    # 3. Predict
    raw_prediction = model.predict(input_data)[0]
    mask = (raw_prediction > confidence_threshold).astype(np.uint8)

    # 4. Create Red Forensic Overlay
    # Create a pure red image
    mask_red = np.zeros_like(img_resized)
    mask_red[:,:,0] = mask[:,:,0] * 255  # Set Red channel to 255 where mask is 1
    
    # Blend original image with red mask
    overlay = cv2.addWeighted(img_resized, 0.7, mask_red, 0.3, 0)

    # 5. Calculate Damage / Area
    oil_pixels = np.count_nonzero(mask)
    area_sq_km = (oil_pixels * 100) / 1_000_000 # 1 pixel = 100m^2
    model_confidence = np.max(raw_prediction) * 100

    # --- DISPLAY RESULTS ---
    
    # Metrics Row
    col1, col2, col3 = st.columns(3)
    col1.metric("Detected Oil Pixels", f"{oil_pixels}")
    col2.metric("Est. Spill Area", f"{area_sq_km:.4f} km²")
    col3.metric("Model Confidence", f"{model_confidence:.1f}%")

    # Images Row
    st.divider()
    col_a, col_b, col_c = st.columns(3)
    
    with col_a:
        st.subheader("1. Satellite Input")
        st.image(img_resized, use_column_width=True)
        
    with col_b:
        st.subheader("2. AI Mask (Binary)")
        st.image(mask * 255, use_column_width=True) # Multiply by 255 to make it white
        
    with col_c:
        st.subheader("3. Forensic Overlay")
        st.image(overlay, use_column_width=True)

    # Severity Warning
    if area_sq_km > 1.0:
        st.error("🚨 CRITICAL SEVERITY: Large scale cleanup required.")
    elif area_sq_km > 0.1:
        st.warning("⚠️ HIGH SEVERITY: Containment booms advised.")
    elif area_sq_km > 0.0:
        st.info("ℹ️ MODERATE SEVERITY: Minor leakage detected.")
    else:
        st.success("✅ NO SPILL DETECTED: Area is clear.")