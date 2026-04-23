# 🌾 Crop Recommendation System using Machine Learning

## 📌 Overview
This project is a **Crop Recommendation System** that suggests the most suitable crop based on soil and environmental conditions. It uses a machine learning model to assist farmers and agricultural planning by making data-driven decisions.

---

## 🚀 Features
- Predicts crop based on:
  - Nitrogen (N)
  - Phosphorus (P)
  - Potassium (K)
  - Temperature
  - Humidity
  - pH value
  - Rainfall
- Built using Random Forest Classifier
- Achieves ~99% accuracy
- Interactive web app using Streamlit
- Handles 22 crop classes

---

## 🧠 Machine Learning Model
- Algorithm: Random Forest
- Type: Multi-class classification
- Evaluation:
  - Accuracy: ~99.5%
  - Macro F1-score: ~0.99
  - 5-Fold Cross Validation used for reliable performance

---

## 📊 Dataset
- Agricultural dataset containing soil nutrients and weather conditions

### Features:
- N, P, K
- Temperature
- Humidity
- pH
- Rainfall

### Target:
- Crop label (22 classes)

---

## ⚙️ Tech Stack
- Python  
- Scikit-learn  
- Pandas  
- Streamlit  
- Joblib  

---

## 🧪 Model Validation
- Train-test split (80/20)
- Cross-validation to ensure generalization
- Checked for:
  - Overfitting
  - Data leakage
  - Duplicate records (none found)

---

## 🌐 Streamlit App

### ▶️ Run Locally
```bash
streamlit run app.py
```
## Author
Muhammad Saim Ansari

🎓 Robotics & Intelligent Systems Student
💻 Aspiring Machine Learning Engineer

📧 Email: saim_ansari2005@outlook.com
