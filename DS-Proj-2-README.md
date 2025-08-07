# 💼 Income Prediction with Census Data

This project builds a **machine learning model** to predict whether an individual's income exceeds **$50K/year** based on demographic and employment-related features from the **Census Income dataset**.

It includes:
- Data preprocessing and exploratory data analysis (EDA)
- Model training and evaluation
- Deployment using a **Flask web application**

---

## 📁 Repository Structure

```
DS-Proj-2/
├── app.py                       # Flask application for model deployment
├── ML_project_live_class.ipynb  # Main development and exploration notebook
├── notebook/
│   └── data/                    # Raw dataset
├── src/                         # Source code for data transformation and modeling
├── templates/                   # HTML templates for Flask UI
├── myenv/                       # Virtual environment (optional, local)
├── requirements.txt             # Project dependencies
├── setup.py                     # Setup configuration
├── .gitignore                   # Git ignore list
├── LICENSE                      # Project license
└── README.md                    # Project documentation
```

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/codewithkaran-21/DS-Proj-2.git
cd DS-Proj-2
```

### 2. (Optional) Create Virtual Environment

```bash
python -m venv myenv
source myenv/bin/activate  # On Windows: myenv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🧠 Project Workflow

1. **Data Loading** – Reads Census dataset and performs initial cleaning.
2. **EDA** – Performed in Jupyter Notebook (`ML_project_live_class.ipynb`).
3. **Preprocessing** – Encoding, scaling, feature selection in `src/` modules.
4. **Model Training** – Trains classification model (e.g., Logistic Regression, Random Forest).
5. **Evaluation** – Accuracy, precision, recall, F1-score, confusion matrix.
6. **Deployment** – Trained model is served via a Flask API in `app.py`.

---

## 🌐 Running the Flask App

```bash
python app.py
```

Once running, visit `http://127.0.0.1:5000/` in your browser to interact with the model.

---

## 📊 Example Features

- Age
- Education Level
- Occupation
- Marital Status
- Hours per week
- Capital Gain/Loss
- Workclass, Race, Gender

---

## 📌 Future Improvements

- [ ] Add Dockerfile for containerized deployment
- [ ] Integrate MLflow for experiment tracking
- [ ] Use DVC for data and model versioning
- [ ] Cloud deployment (AWS/GCP/Azure)
- [ ] Improve front-end styling with Bootstrap or CSS

---

## 🧑‍💻 Author

**Karan Singh**  
GitHub: [@codewithkaran-21](https://github.com/codewithkaran-21)

---

## 📄 License

Licensed under the [MIT License](LICENSE).