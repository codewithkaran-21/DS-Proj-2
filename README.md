# Income Classification (Census Data)

A production-ready machine learning project that predicts whether an individual's annual income exceeds $50K using Census (Adult) data. This repository contains exploratory analysis, preprocessing, model training, and a small Flask app to serve the trained model for real-time predictions.

Table of Contents
- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Key Features](#key-features)
- [Repository Structure](#repository-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Quick Install](#quick-install)
  - [Preparing the Data](#preparing-the-data)
  - [Training the Model](#training-the-model)
  - [Running the Flask App](#running-the-flask-app)
- [Usage Examples](#usage-examples)
  - [Web Form (Interactive)](#web-form-interactive)
  - [API (Programmatic)](#api-programmatic)
- [Modeling & Evaluation](#modeling--evaluation)
- [Possible Enhancements](#possible-enhancements)
- [Contributing](#contributing)
- [License](#license)
- [Author & Contact](#author--contact)
- [Acknowledgements](#acknowledgements)

## Project Overview
This project demonstrates an end-to-end ML workflow:
- Ingest Census (Adult) data
- Explore and clean data (EDA)
- Feature engineering and preprocessing (encoding, scaling, selection)
- Train and evaluate classification models (e.g., Logistic Regression, Random Forest)
- Serve predictions via a lightweight Flask app for simple real-time inference

The aim is to provide a clear, replicable pipeline suitable for learning and lightweight demos.

## Dataset
This project uses the UCI "Adult" / Census Income dataset. It contains demographic features and is commonly used to predict whether income exceeds $50K/year.

Typical columns include:
- age, workclass, education, marital-status, occupation, race, sex, hours-per-week, capital-gain, capital-loss, etc.

(Place the raw dataset CSV files in `notebook/data/` as shown in this repository.)

## Key Features Used
- Age
- Education Level
- Workclass
- Occupation
- Marital Status
- Hours per week
- Race
- Sex
- Capital Gain / Loss

## Repository Structure
- app.py — Flask application for serving the trained model
- ML_project_live_class.ipynb — Notebook for EDA, training, and evaluation
- notebook/data/ — Raw dataset files (CSV/ TXT)
- src/ — Python source modules for ingestion, preprocessing, modeling (transformers, pipelines)
- templates/ — HTML templates used by Flask for the web form
- requirements.txt — Python dependencies
- setup.py — Optional packaging script
- .gitignore — Files and folders ignored by Git
- LICENSE — MIT License

## Getting Started

### Prerequisites
- Python 3.8+
- pip
- (Optional) virtualenv or venv
- Git

### Quick Install
1. Clone the repository
   git clone https://github.com/codewithkaran-21/DS-Proj-2.git
   cd DS-Proj-2

2. (Optional) Create & activate a virtual environment
   python -m venv myenv
   # Windows
   myenv\Scripts\activate
   # macOS / Linux
   source myenv/bin/activate

3. Install dependencies
   pip install -r requirements.txt

### Preparing the Data
- Place the raw Census (Adult) dataset files under `notebook/data/` (the notebook expects data there).
- Open `ML_project_live_class.ipynb` to run the full exploratory analysis, preprocessing and model training steps. The notebook walks through missing value handling, encoding, scaling and model evaluation.

### Training the Model
- The primary training flow is demonstrated in `ML_project_live_class.ipynb`. Follow the cells to:
  - Load data from `notebook/data/`
  - Preprocess (encoding, scaling)
  - Train chosen models (Logistic Regression, Random Forest, etc.)
  - Evaluate and persist the best model (e.g., `models/model.pkl`)

If `src/` contains training scripts or a defined training entrypoint, those can be used as an alternative to the notebook.

### Running the Flask App
1. Ensure a trained model artifact exists (the Flask app loads a serialized model file — see notebook or src for default save path).
2. Start the app:
   python app.py
3. Open your browser to:
   http://127.0.0.1:5000/
4. Use the provided web form to enter feature values and obtain a prediction.

If you prefer to call the app programmatically, review `app.py` to find the API route(s) available for POST requests.

## Usage Examples

Web form (interactive)
- Visit the root URL after starting the Flask server, complete the fields and submit to see an income prediction.

API (programmatic)
- If the app exposes a prediction endpoint (e.g., `/predict`), send a JSON payload such as:
  {
    "age": 37,
    "workclass": "Private",
    "education": "Bachelors",
    "occupation": "Exec-managerial",
    "marital_status": "Married-civ-spouse",
    "hours_per_week": 40,
    "race": "White",
    "sex": "Male",
    "capital_gain": 0,
    "capital_loss": 0
  }
- The endpoint will return a predicted label and (optionally) class probabilities depending on implementation.

Note: Check `app.py` for exact endpoint path and input schema.

## Modeling & Evaluation
- Models evaluated: Logistic Regression, Random Forest (examples — see notebook)
- Metrics reported: Accuracy, Precision, Recall, F1-score. Confusion matrix and classification reports are generated in the notebook.
- Use cross-validation and hold-out test set to validate the generalization performance.

## Possible Enhancements
- Add unit and integration tests for preprocessing, model code, and Flask routes
- Containerize with Docker for consistent deployment
- Experiment tracking with MLflow or Weights & Biases
- Add automated data & model versioning with DVC
- Deploy to a cloud provider (Heroku, AWS Elastic Beanstalk, GCP Cloud Run, Azure App Service)
- Add CI/CD to train, test, and redeploy models automatically

## Contributing
Contributions are welcome. Suggested workflow:
1. Fork the repository
2. Create a feature branch (git checkout -b feature/my-feature)
3. Implement changes and tests
4. Open a pull request describing your change and rationale

Please follow repository coding style and add tests where applicable.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author & Contact
Karan Singh  
GitHub: [codewithkaran-21](https://github.com/codewithkaran-21)

## Acknowledgements
- UCI Machine Learning Repository — Adult dataset
- Any libraries used (scikit-learn, pandas, Flask, etc.)

Thank you for taking a look — if you'd like, I can:
- Add a CONTRIBUTING.md and issue/pr templates
- Create a Dockerfile and docker-compose example
- Expand the README with example API request/response examples derived from app.py