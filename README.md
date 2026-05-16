# 📊 TELECOM CUSTOMER CHURN PREDICTION

---

## 📌 PROJECT OVERVIEW

Customer churn is one of the biggest challenges in the telecom industry. Losing existing customers directly affects company revenue and business growth.

This project predicts whether a telecom customer is likely to churn using Machine Learning, Data Analysis, SHAP Explainability, and Streamlit deployment.

The system analyzes:
- Customer demographics
- Billing details
- Internet services
- Contract information
- Payment behavior

to predict churn risk and provide business insights.

---

# 🎯 PROBLEM STATEMENT

The main objective of this project is to:
- Analyze customer churn behavior
- Identify major churn-driving factors
- Build predictive machine learning models
- Provide retention recommendations

---

# 🛠️ TECHNOLOGIES USED

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- SMOTE
- SHAP
- Streamlit

---

# 📂 DATASET INFORMATION

Dataset Used:
- Telco Customer Churn Dataset

Important features include:
- Monthly Charges
- Contract Type
- Internet Service
- Payment Method
- Customer Tenure
- Technical Support
- Churn Status

---

# 🔍 PROJECT WORKFLOW

## 1️⃣ DATA UNDERSTANDING

- Checked dataset structure
- Analyzed datatypes and missing values
- Understood categorical and numerical features

---

## 2️⃣ DATA CLEANING

- Handled missing values
- Converted `Total Charges` into numeric datatype
- Removed unnecessary columns
- Fixed datatype inconsistencies

---

## 3️⃣ EXPLORATORY DATA ANALYSIS (EDA)

EDA was performed to identify important customer behavior patterns.

### 📈 KEY INSIGHTS

- Customers with higher monthly charges churned more.
- Customers with shorter tenure were more likely to churn.
- Month-to-month contract customers showed higher churn.
- Electronic check users showed higher churn tendency.
- Customers without tech support were more likely to leave.

---

# ⚙️ FEATURE ENGINEERING

Additional features were created to improve model learning:
- Tenure Group
- Total Services
- Average Monthly Spend
- New Customer Indicator

---

# 🤖 MODEL BUILDING

## 🔹 LOGISTIC REGRESSION

Logistic Regression was first used as the baseline model because it is simple, interpretable, and suitable for binary classification.

However, the dataset was imbalanced:
- non-churn customers were much higher than churn customers.

Because of this imbalance:
- the model achieved decent accuracy,
- but churn recall was not strong enough.

---

## 🔹 RANDOM FOREST CLASSIFIER

Random Forest was then used to improve performance.

Reason:
- handles complex relationships better,
- captures feature interactions,
- performs well for classification problems.

However, overall improvement was limited and churn prediction did not improve significantly.

---

## 🔹 HANDLING IMBALANCE USING SMOTE

The dataset contained fewer churn customers than non-churn customers.

To solve this imbalance issue:
- SMOTE (Synthetic Minority Oversampling Technique) was applied.

After applying SMOTE:
- churn detection improved,
- recall became better,
- but precision slightly decreased.

This is a common tradeoff in churn prediction problems.

---

# ✅ FINAL MODEL SELECTION

The final approach used:
- Logistic Regression
- with SMOTE-balanced training data

Reason:
- balanced performance,
- better churn detection,
- stable predictions,
- easier interpretability.

---

# 📉 MODEL PERFORMANCE

| Metric | Score |
|---|---|
| Accuracy | 79% |
| Recall | 61% |
| ROC-AUC | 0.84 |

---

# 🧠 SHAP EXPLAINABILITY

SHAP was used to understand how different features influenced churn prediction.

### 🔑 MAJOR CHURN DRIVERS

- Monthly Charges
- Tenure Months
- Internet Service
- Payment Method
- Contract Type

---

# 🌐 STREAMLIT DASHBOARD

An interactive Streamlit app was developed to:
- predict churn risk,
- show churn probability,
- and provide retention recommendations.

---

# 💡 BUSINESS RECOMMENDATIONS

Based on the analysis:
- Offer loyalty discounts
- Encourage long-term contracts
- Improve technical support
- Focus on retaining new customers
- Monitor high monthly charge customers

---

# 📸 PROJECT SCREENSHOTS

All important screenshots including:
- EDA Visualizations
- ROC Curve
- Confusion Matrix
- SHAP Summary Plot
- Streamlit Dashboard Outputs

are properly included inside the `screenshots/` folder in the project directory.

---

# 📁 PROJECT STRUCTURE

```text
TELECOM-CHURN-PREDICTION/
│
├── app/
├── data/
├── models/
├── notebooks/
├── screenshots/
├── reports/
├── README.md
└── requirements.txt
```

---

# ▶️ HOW TO RUN THE PROJECT

### Install Requirements

- pip install -r requirements.txt

### Run Streamlit App

- streamlit run app/app.py

---

# 📌 CONCLUSION

This project successfully built an end-to-end telecom customer churn prediction system using:
- Machine Learning
- SMOTE balancing
- SHAP Explainability
- Streamlit deployment

The project not only predicts churn but also explains the important factors influencing customer behavior, helping telecom companies improve customer retention strategies.