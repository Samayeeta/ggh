import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import tensorflow as tf
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io
import cv2
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

# Load the CNN model
model = tf.keras.models.load_model("models/cic_cnn.h5")

def preprocess_image(image):
    img = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    img = cv2.resize(img, (128, 128))
    img = img / 255.0
    return np.expand_dims(img, axis=0)

def analyze_image(image):
    processed_image = preprocess_image(image)
    prediction = model.predict(processed_image)[0][0]
    return prediction

def analyze_patient_data(patient_data):
    risk_factors = 0
    if patient_data['Hypertension'] == 'Yes':
        risk_factors += 1
    if patient_data['Diabetes'] == 'Yes':
        risk_factors += 1
    if patient_data['Symptoms'] in ['Shortness of breath', 'Swelling in legs']:
        risk_factors += 1
    if patient_data['Cancer Stage'] in ['Stage III', 'Stage IV']:
        risk_factors += 1

    if risk_factors >= 2:
        return "High Risk"
    else:
        return "Low Risk"

def generate_report(image_analysis, patient_risk, patient_data, lvef, heart_size):
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    c.drawString(100, 750, "CardioLens Report")
    c.drawString(100, 700, f"Image Analysis: {image_analysis:.2f} (Probability of CIC)")
    c.drawString(100, 680, f"Patient Risk: {patient_risk}")
    c.drawString(100, 660, f"Age: {patient_data['Age']}")
    c.drawString(100, 640, f"Chemo Drug: {patient_data['Chemo Drug']}")
    c.drawString(100, 620, f"Total Dose: {patient_data['Total Dose']}")
    c.drawString(100, 600, f"Hypertension: {patient_data['Hypertension']}")
    c.drawString(100, 580, f"Diabetes: {patient_data['Diabetes']}")
    c.drawString(100, 560, f"Symptoms: {patient_data['Symptoms']}")
    c.drawString(100, 540, f"Cancer Stage: {patient_data['Cancer Stage']}")
    c.drawString(100, 520, f"Cancer Free: {patient_data['Cancer Free']}")
    c.drawString(100, 500, f"Left Ventricular Ejection Fraction (Simulated): {lvef}%")
    c.drawString(100, 480, f"Heart Size (Simulated): {heart_size} mm")
    c.save()
    buffer.seek(0)
    return buffer

def analyze_cic_image(image):
    img = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    img = cv2.resize(img, (200, 200))

    simulated_lvef = np.random.randint(40, 60)
    simulated_size = np.random.randint(50, 70)

    return simulated_lvef, simulated_size

def train_and_evaluate_model(image_paths, labels):
    images = []
    for img_path in image_paths:
        img = cv2.imread(img_path)
        img = cv2.resize(img, (128, 128))
        img = img / 255.0
        images.append(img)
    images = np.array(images)
    labels = np.array(labels)

    X_train, X_test, y_train, y_test = train_test_split(images, labels, test_size=0.2, random_state=42)

    model.fit(X_train, y_train, epochs=10, validation_data=(X_test, y_test))

    y_pred = model.predict(X_test)
    y_pred_binary = (y_pred > 0.5).astype(int)

    accuracy = accuracy_score(y_test, y_pred_binary)
    return accuracy

def main():
    st.title("CardioLens: CIC Diagnostic Assistant")

    uploaded_image = st.file_uploader("Upload Echocardiogram Image", type=["jpg", "png", "jpeg"])

    age = st.number_input("Age", min_value=18, max_value=120, value=60)
    chemo_drug = st.selectbox("Chemo Drug", ["Doxorubicin", "Trastuzumab", "Other"])
    total_dose = st.number_input("Total Dose", min_value=100, value=300)
    hypertension = st.selectbox("Hypertension", ["Yes", "No"])
    diabetes = st.selectbox("Diabetes", ["Yes", "No"])
    symptoms = st.selectbox("Symptoms", ["None", "Shortness of breath", "Swelling in legs", "Other"])
    cancer_stage = st.selectbox("Cancer Stage", ["Stage I", "Stage II", "Stage III", "Stage IV", "Cancer Free"])
    cancer_free = st.selectbox("Cancer Free", ["Yes", "No"])

    if st.button("Analyze"):
        if uploaded_image:
            image = Image.open(uploaded_image)
            image_analysis = analyze_image(image)
            patient_data = {
                "Age": age,
                "Chemo Drug": chemo_drug,
                "Total Dose": total_dose,
                "Hypertension": hypertension,
                "Diabetes": diabetes,
                "Symptoms": symptoms,
                "Cancer Stage": cancer_stage,
                "Cancer Free": cancer_free,
            }

            patient_risk = analyze_patient_data(patient_data)
            lvef, heart_size = analyze_cic_image(image)

            st.image(image, caption="Uploaded Echocardiogram", use_column_width=True)
            st.write(f"Probability of CIC: {image_analysis:.2f}")
            st.write(f"Patient Risk: {patient_risk}")
            st.write(f"Left Ventricular Ejection Fraction (Simulated): {lvef}%")
            st.write(f"Heart Size (Simulated): {heart_size} mm")

            report_buffer = generate_report(image_analysis, patient_risk, patient_data, lvef, heart_size)
            st.download_button(
                label="Download Report",
                data=report_buffer,
                file_name="cardiolens_report.pdf",
                mime="application/pdf",
            )
        else:
            st.warning("Please upload an image.")

    if st.button("Train Model"):
        image_paths = ["data/img1.jpg", "data/img2.jpg"]  # Replace with your actual paths
        labels = [0, 1]  # Replace with your actual labels (0: no CIC, 1: CIC)
        accuracy = train_and_evaluate_model(image_paths, labels)
        st.write(f"Model Accuracy: {accuracy:.2f}")

if __name__ == "__main__":
    main()