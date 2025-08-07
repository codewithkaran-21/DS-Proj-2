# 💼 Income Classification - Census Data Project

This project builds a machine learning model to **predict whether an individual's income exceeds $50K per year** based on census data. It covers all stages of the ML lifecycle — from data ingestion and preprocessing to model training, evaluation, and deployment via a Flask web application.

---

## 🎯 Project Goals

- Understand and explore the **Census Income** dataset.
- Preprocess data and perform feature engineering.
- Train and evaluate a classifier to predict income class (`<=50K` or `>50K`).
- Deploy the trained model using a **Flask API** for real-time inference.

---

## 📁 Project Structure

```
DS-Proj-2/
├── app.py                       # Flask application for model inference
├── ML_project_live_class.ipynb  # Notebook for EDA, training and testing
├── notebook/
│   └── data/                    # Raw dataset (.csv, .txt, etc.)
├── src/                         # Core ML pipeline: ingestion, transformation, modeling
├── templates/                   # HTML templates used by Flask
├── myenv/                       # Virtual environment (can be ignored in version control)
├── requirements.txt             # Python dependencies
├── setup.py                     # Install script for packaging the project
├── .gitignore                   # Git ignore rules
├── LICENSE                      # License information (MIT)
└── README.md                    # Project documentation (this file)
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/codewithkaran-21/DS-Proj-2.git
cd DS-Proj-2
```

### 2. (Optional) Create and Activate Virtual Environment

```bash
python -m venv myenv
# Activate:
# On Windows:
myenv\Scripts\activate
# On Unix or MacOS:
source myenv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🧠 Project Workflow

1. **Data Ingestion**  
   Load census data from local files (under `notebook/data/`) into your ML pipeline.

2. **Exploratory Data Analysis (EDA)**  
   Conducted in the Jupyter Notebook `ML_project_live_class.ipynb` — includes feature exploration, missing value handling, and outlier detection.

3. **Data Preprocessing**  
   Performed in `src/` modules: encoding, scaling, train-test split, and feature selection.

4. **Model Training & Evaluation**  
   Train classification models (e.g., Logistic Regression, Random Forest, etc.) and evaluate them using accuracy, precision, recall, F1-score.

5. **Model Deployment**  
   A trained model is loaded and served using a Flask application via `app.py`.

---

## 🌐 Running the Flask App

Once your model is trained and saved, run:

```bash
python app.py
```

Then open your browser and go to:

```
http://127.0.0.1:5000/
```

You can enter feature values through the web form and receive income predictions in real-time.

---

## 🧪 Features Used in Prediction

- Age  
- Education Level  
- Workclass  
- Occupation  
- Marital Status  
- Hours per week  
- Race and Sex  
- Capital Gain/Loss  

---

## 📌 Possible Enhancements

- [ ] Add unit tests for model and Flask routes  
- [ ] Add Docker support for containerization  
- [ ] Log experiments with MLflow  
- [ ] Integrate DVC for data and model versioning  
- [ ] Deploy on cloud using AWS/GCP/Azure  

---

## 🧑‍💻 Author

**Karan Singh**  
[GitHub Profile](https://github.com/codewithkaran-21)

---

## 📄 License

This project is licensed under the **MIT License** – see the [LICENSE](./LICENSE) file for details.