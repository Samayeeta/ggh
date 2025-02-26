# CardioGuardAI: Empowering Cardio-Oncology with AI-Driven Diagnostics

## The Urgent Need for Advanced Cardio-Oncology Diagnostics

Noncommunicable diseases (NCDs), encompassing cardiovascular diseases (CVDs), cancers, and more, account for approximately 60% of global deaths, according to the National Library of Medicine. CVDs, specifically ischaemic heart disease, are the leading cause, contributing to 17.7 million deaths annually. In India, the situation is particularly critical; the World Health Organization reports that India accounts for one-fifth of global CVD deaths, disproportionately affecting younger individuals. The Global Burden of Disease study reveals an age-standardized CVD death rate of 272 per 100,000 in India, significantly exceeding the global average of 235 per 100,000.

CardioGuardAI directly addresses this urgent need by providing an AI-powered diagnostic assistant designed to aid cardio-oncologists in the early detection and management of Chemotherapy-Induced Cardiomyopathy (CIC). This is especially vital in high-volume settings, such as Indian government hospitals, where rapid and accurate diagnostics are crucial for patient care.

## Problem Statement (Google Girl Hackathon - Ideation Stage)

**Medicine:** Develop a diagnostic assistant that leverages medical images, patient data, and symptom analysis to support healthcare professionals in accurate and efficient disease diagnosis, utilizing mock data.

## What CardioGuardAI Offers

* **Echocardiogram Image Analysis:** Employs a Convolutional Neural Network (CNN) to analyze echocardiogram images, identifying potential markers of CIC.
* **Comprehensive Patient Data Input:** Features an intuitive form to collect detailed patient information, including demographics, chemotherapy regimen, comorbidities, and symptoms.
* **Dynamic Data Updates:** Patient data is immediately written to a `data/patient_data.csv` file upon completion of the form, allowing for data tracking and analysis.
* **AI-Driven Risk Assessment:** Integrates image analysis and patient data to generate a risk assessment for CIC.
* **Detailed PDF Report Generation:** Produces a professional, styled PDF report summarizing the analysis and patient information.

## How CardioGuardAI Functions

1.  **Image Upload:** Users upload an echocardiogram image for analysis.
2.  **Patient Data Entry:** Users complete a detailed patient information form.
3.  **Image Processing:** The CNN processes the uploaded image to identify relevant features.
4.  **Data Integration and Risk Calculation:** Patient data and image analysis results are combined to calculate the CIC risk.
5.  **Report Generation:** A PDF report is generated, providing a comprehensive analysis.

## AI Implementation

* **Convolutional Neural Network (CNN):**
    * Implemented using TensorFlow/Keras.
    * Trained on a dataset of echocardiogram images (mock data for this prototype).
    * Analyzes images to detect patterns indicative of CIC.
    * Outputs a probability score representing the likelihood of CIC.

## Importance for Cardio-Oncologists

Cardio-oncologists specialize in managing the cardiac complications of cancer therapies. CardioGuardAI enhances their practice by:

* **Improving Diagnostic Accuracy:** AI-driven analysis supplements clinical expertise.
* **Facilitating Early Intervention:** Early detection of CIC leads to better patient outcomes.
* **Enhancing Workflow Efficiency:** Automates analysis and report generation, saving time.

## Why AI is Essential in India

* **High Patient Throughput:** AI automates diagnostics, enabling efficient handling of large patient volumes.
* **Accessibility of Expertise:** AI assists in areas with limited specialized expertise.
* **Standardized Diagnostics:** AI ensures consistent and objective analysis.

## Tech Stack

* **Python:** Core programming language.
* **Streamlit:** For building the interactive web application.
* **TensorFlow/Keras:** For implementing the CNN.
* **Pandas:** For data manipulation and analysis.
* **ReportLab:** For PDF report generation.
* **Scikit-learn:** For model evaluation.
* **Pillow (PIL):** For image handling.
* **CSV:** For data storage.

## How to Run CardioGuardAI

### Prerequisites

* Python 3.7+
* Pip
* Virtual environment (recommended)

### Installation

1.  **Clone the repository:**

    ```bash
    git clone [your-repository-url]
    cd CardioGuardAI
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**

    * On Windows: `venv\Scripts\activate`
    * On macOS/Linux: `source venv/bin/activate`

4.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

5.  **Create the model:**

    ```bash
    python create_model.py
    ```

6.  **Run the application:**

    ```bash
    streamlit run app.py
    ```

### Usage

1.  Open the Streamlit app in your browser.
2.  Upload an echocardiogram image.
3.  Fill out the patient data form.
4.  Click "Analyze."
5.  Download the generated PDF report.

## Note

This prototype uses mock data for demonstration. For real-world applications, a comprehensive dataset is essential for training a robust CNN model.

## Future Developments

* Integration with Electronic Health Records (EHRs).
* Advanced Natural Language Processing (NLP) for symptom analysis.
* Expansion of the training dataset for improved model accuracy.
* Implementation of advanced AI algorithms.
* Addressing bias in AI models.