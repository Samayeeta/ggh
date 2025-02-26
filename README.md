# CardioGuardAI: AI-Powered CIC Diagnostic Assistant

[![Heart Emoticon](https://img.shields.io/badge/%F0%9F%A7%A1-CardioGuardAI-red)](https://streamlit.io/)

**CardioGuardAI** is a Streamlit-based prototype designed to assist cardio-oncologists in the early detection and risk assessment of Chemotherapy-Induced Cardiomyopathy (CIC). By integrating echocardiogram image analysis with patient data and symptom evaluation, this tool aims to streamline diagnostic workflows and improve patient outcomes.

## Why CardioGuardAI?

Cardio-oncology is a critical field, focusing on the cardiovascular health of cancer patients undergoing treatment. Cardio-oncologists play a vital role in mitigating the cardiac side effects of cancer therapies, which can significantly impact patient quality of life and survival.

**The Need for AI:**

* **Early Detection:** AI algorithms can analyze complex data patterns to identify patients at high risk of CIC earlier than traditional methods.
* **Efficiency in High-Volume Settings:** In countries like India, where government hospitals face a massive influx of patients, AI-driven tools can significantly reduce the burden on healthcare professionals.
* **Data-Driven Insights:** AI can process and interpret large datasets of clinical and imaging data, providing valuable insights for personalized treatment plans.
* **Reducing Disparities:** When trained on diverse datasets, AI can help reduce healthcare disparities and ensure equitable access to quality care.

**Statistics Highlighting the Importance:**

* Cardiovascular complications are a leading cause of morbidity and mortality in cancer survivors.
* Studies indicate that up to 30% of patients receiving certain chemotherapy drugs experience cardiac dysfunction.
* In India, the burden of cancer and cardiovascular diseases is substantial. Government hospitals often see hundreds of patients daily, making efficient diagnostic tools essential.
* Research shows that early detection of CIC can improve patient outcomes by up to 40%.
* According to a study published in the Journal of the American College of Cardiology, AI algorithms can predict cardiotoxicity with an accuracy of up to 85%.

**Racial and Ethnic Considerations:**

* It is crucial to acknowledge potential biases in AI algorithms. If trained on limited, homogenous datasets, AI can perpetuate and exacerbate healthcare disparities.
* For Example, a study from the National Institutes of Health (NIH) showed that some AI algorithms performed less accurately in predicting cardiovascular risk in African American populations.
* To mitigate this, CardioGuardAI emphasizes the importance of diverse training data and continuous validation.

**How CardioGuardAI Is Better:**

While other applications and ideas exist in the realm of AI-driven medical diagnostics, CardioGuardAI distinguishes itself through:

* **Integrated Approach:** It combines image analysis with patient data and symptom evaluation for a holistic risk assessment.
* **User-Friendly Interface:** Streamlit provides a simple and intuitive interface, making it easy for clinicians to use.
* **Customizable Reporting:** The PDF report generation allows for easy documentation and communication of findings.
* **Focus on Cardio-Oncology:** CardioGuardAI is specifically tailored to the unique needs of cardio-oncologists.

## Getting Started

### Prerequisites

* Python 3.7+
* Pip
* Virtual environment (recommended)

### Installation

1.  **Clone the repository:**

    ```bash
    git clone [repository URL]
    cd CardioGuardAI
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python -m venv venv
    # Activate the virtual environment
    # On Windows:
    venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

1.  **Run the Streamlit app:**

    ```bash
    streamlit run app.py
    ```

2.  Open your web browser and navigate to the URL displayed in the terminal.

### Project Structure

CardioGuardAI/
├── app.py
├── data/
│   ├── img1.jpg
│   ├── img2.jpg
│   └── patient_data.csv
├── models/
│   └── cic_cnn.h5
├── requirements.txt
└── README.md


### Usage

1.  Upload an echocardiogram image.
2.  Fill in the patient data form.
3.  Click "Analyze."
4.  Download the generated PDF report.

### Model Training

* The `models/cic_cnn.h5` model is a basic CNN. For real-world applications, a more robust model trained on a larger dataset is recommended.
* The `create_model.py` file within the code, contains the code that creates the model.

### Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bug fixes or feature requests.

### License

[MIT License]

### Contact

[Your Email/Contact Information]