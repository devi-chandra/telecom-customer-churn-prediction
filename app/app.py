import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Telecom Customer Churn Prediction",
    layout="wide"
)

model = joblib.load('models/churn_model.pkl')

st.title("Telecom Customer Churn Prediction Dashboard")

st.markdown(
    "Predict whether a telecom customer is likely to churn based on customer details and telecom services."
)

st.sidebar.header("Model Performance")

st.sidebar.metric("Accuracy", "79%")
st.sidebar.metric("Recall", "61%")
st.sidebar.metric("ROC-AUC", "0.84")

st.sidebar.markdown("---")

st.sidebar.write(
    "Model: Logistic Regression + SMOTE"
)

st.header("Customer Information")

col1, col2 = st.columns(2)

with col1:

    tenure = st.number_input(
        "Tenure Months",
        min_value=0,
        value=1
    )

    monthly_charges = st.number_input(
        "Monthly Charges",
        min_value=0.0,
        value=95.0
    )

    total_charges = st.number_input(
        "Total Charges",
        min_value=0.0,
        value=120.0
    )

    cltv = st.number_input(
        "CLTV",
        min_value=0,
        value=2000
    )

    gender = st.selectbox(
        "Gender",
        ["Female", "Male"]
    )

    senior_citizen = st.selectbox(
        "Senior Citizen",
        ["No", "Yes"]
    )

    partner = st.selectbox(
        "Partner",
        ["No", "Yes"]
    )

    dependents = st.selectbox(
        "Dependents",
        ["No", "Yes"]
    )

    phone_service = st.selectbox(
        "Phone Service",
        ["No", "Yes"]
    )

    multiple_lines = st.selectbox(
        "Multiple Lines",
        ["No", "Yes", "No phone service"]
    )

with col2:

    internet_service = st.selectbox(
        "Internet Service",
        ["DSL", "Fiber optic", "No"]
    )

    online_security = st.selectbox(
        "Online Security",
        ["No", "Yes", "No internet service"]
    )

    online_backup = st.selectbox(
        "Online Backup",
        ["No", "Yes", "No internet service"]
    )

    device_protection = st.selectbox(
        "Device Protection",
        ["No", "Yes", "No internet service"]
    )

    tech_support = st.selectbox(
        "Tech Support",
        ["No", "Yes", "No internet service"]
    )

    streaming_tv = st.selectbox(
        "Streaming TV",
        ["No", "Yes", "No internet service"]
    )

    streaming_movies = st.selectbox(
        "Streaming Movies",
        ["No", "Yes", "No internet service"]
    )

    contract = st.selectbox(
        "Contract",
        ["Month-to-month", "One year", "Two year"]
    )

    paperless_billing = st.selectbox(
        "Paperless Billing",
        ["No", "Yes"]
    )

    payment_method = st.selectbox(
        "Payment Method",
        [
            "Electronic check",
            "Mailed check",
            "Bank transfer (automatic)",
            "Credit card (automatic)"
        ]
    )

if st.button("Predict Churn"):

    input_data = {
        'Tenure Months': tenure,
        'Monthly Charges': monthly_charges,
        'Total Charges': total_charges,
        'CLTV': cltv,

        'Gender_Male': 1 if gender == "Male" else 0,

        'Senior Citizen_Yes': 1 if senior_citizen == "Yes" else 0,

        'Partner_Yes': 1 if partner == "Yes" else 0,

        'Dependents_Yes': 1 if dependents == "Yes" else 0,

        'Phone Service_Yes': 1 if phone_service == "Yes" else 0,

        'Multiple Lines_Yes': 1 if multiple_lines == "Yes" else 0,
        'Multiple Lines_No phone service': 1 if multiple_lines == "No phone service" else 0,

        'Internet Service_Fiber optic': 1 if internet_service == "Fiber optic" else 0,
        'Internet Service_No': 1 if internet_service == "No" else 0,

        'Online Security_Yes': 1 if online_security == "Yes" else 0,
        'Online Security_No internet service': 1 if online_security == "No internet service" else 0,

        'Online Backup_Yes': 1 if online_backup == "Yes" else 0,
        'Online Backup_No internet service': 1 if online_backup == "No internet service" else 0,

        'Device Protection_Yes': 1 if device_protection == "Yes" else 0,
        'Device Protection_No internet service': 1 if device_protection == "No internet service" else 0,

        'Tech Support_Yes': 1 if tech_support == "Yes" else 0,
        'Tech Support_No internet service': 1 if tech_support == "No internet service" else 0,

        'Streaming TV_Yes': 1 if streaming_tv == "Yes" else 0,
        'Streaming TV_No internet service': 1 if streaming_tv == "No internet service" else 0,

        'Streaming Movies_Yes': 1 if streaming_movies == "Yes" else 0,
        'Streaming Movies_No internet service': 1 if streaming_movies == "No internet service" else 0,

        'Contract_One year': 1 if contract == "One year" else 0,
        'Contract_Two year': 1 if contract == "Two year" else 0,

        'Paperless Billing_Yes': 1 if paperless_billing == "Yes" else 0,

        'Payment Method_Credit card (automatic)': 1 if payment_method == "Credit card (automatic)" else 0,

        'Payment Method_Electronic check': 1 if payment_method == "Electronic check" else 0,

        'Payment Method_Mailed check': 1 if payment_method == "Mailed check" else 0
    }

    input_df = pd.DataFrame([input_data])

    expected_columns = model.feature_names_in_

    input_df = input_df.reindex(
        columns=expected_columns,
        fill_value=0
    )

    input_df = input_df.astype(float)

    probability = model.predict_proba(input_df)[0][1]

    st.subheader("Prediction Result")

    st.write(f"Raw Churn Probability: {probability:.4f}")

    if probability >= 0.50:

        st.error(
            f"High Churn Risk\n\nChurn Probability: {probability:.2%}"
        )

        st.write("Recommended Retention Actions:")
        st.write("- Offer loyalty discounts")
        st.write("- Improve technical support")
        st.write("- Suggest yearly contract plans")
        st.write("- Provide customer engagement offers")

    elif probability >= 0.30:

        st.warning(
            f"Medium Churn Risk\n\nChurn Probability: {probability:.2%}"
        )

        st.write("Recommended Actions:")
        st.write("- Monitor customer satisfaction")
        st.write("- Send personalized offers")

    else:

        st.success(
            f"Low Churn Risk\n\nChurn Probability: {probability:.2%}"
        )

        st.write("Customer is likely to stay.")

    st.markdown("---")

    st.subheader("Key Churn Indicators")

    if monthly_charges > 80:
        st.write("- High monthly charges may increase churn risk.")

    if tenure < 12:
        st.write("- New customers are more likely to churn.")

    if contract == "Month-to-month":
        st.write("- Month-to-month contracts showed higher churn.")

    if payment_method == "Electronic check":
        st.write("- Electronic check users had relatively higher churn.")

    if tech_support == "No":
        st.write("- Lack of tech support may increase churn probability.")

    if internet_service == "Fiber optic":
        st.write("- Fiber optic customers showed higher churn trends.")