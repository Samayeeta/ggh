import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import tensorflow as tf
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph, SimpleDocTemplate
import io
import cv2

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

def generate_styled_report(image_analysis, patient_risk, patient_data, lvef, heart_size):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    styles = getSampleStyleSheet()
    title_style = styles['Title']
    heading_style = styles['Heading2']
    text_style = styles['Normal']

    elements = []
    elements.append(Paragraph("CardioGuardAI Report", title_style))
    elements.append(Paragraph(f"Image Analysis: {image_analysis:.2f} (Probability of CIC)", text_style))
    elements.append(Paragraph(f"Patient Risk: {patient_risk}", text_style))
    elements.append(Paragraph("Patient Details", heading_style))
    elements.append(Paragraph(f"Age: {patient_data['Age']}", text_style))
    elements.append(Paragraph(f"Chemo Drug: {patient_data['Chemo Drug']}", text_style))
    elements.append(Paragraph(f"Total Dose: {patient_data['Total Dose']}", text_style))
    elements.append(Paragraph(f"Hypertension: {patient_data['Hypertension']}", text_style))
    elements.append(Paragraph(f"Diabetes: {patient_data['Diabetes']}", text_style))
    elements.append(Paragraph(f"Symptoms: {patient_data['Symptoms']}", text_style))
    elements.append(Paragraph(f"Cancer Stage: {patient_data['Cancer Stage']}", text_style))
    elements.append(Paragraph(f"Cancer Free: {patient_data['Cancer Free']}", text_style))
    elements.append(Paragraph("Echocardiogram Analysis", heading_style))
    elements.append(Paragraph(f"Left Ventricular Ejection Fraction (Simulated): {lvef}%", text_style))
    elements.append(Paragraph(f"Heart Size (Simulated): {heart_size} mm", text_style))

    doc.build(elements)
    buffer.seek(0)
    return buffer

def analyze_cic_image(image):
    img = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    img = cv2.resize(img, (200, 200))

    simulated_lvef = np.random.randint(40, 60)
    simulated_size = np.random.randint(50, 70)

    return simulated_lvef, simulated_size

def main():
    st.set_page_config(page_title="CardioGuardAI", page_icon="❤️")
    st.title("CardioGuardAI: CIC Diagnostic Assistant")
    st.write("CardioGuardAI is a diagnostic tool designed to assist cardio-oncologists in the assessment of Chemotherapy-Induced Cardiomyopathy (CIC). By analyzing echocardiogram images and patient data, it provides risk assessments and generates detailed reports.")


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

            report_buffer = generate_styled_report(image_analysis, patient_risk, patient_data, lvef, heart_size)
            st.download_button(
                label="Download Report",
                data=report_buffer,
                file_name="cardioguardai_report.pdf",
                mime="application/pdf",
            )
        else:
            st.warning("Please upload an image.")

if __name__ == "__main__":
    main()