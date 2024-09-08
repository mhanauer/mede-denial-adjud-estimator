import streamlit as st
import pandas as pd
import numpy as np

# Generate Sample Data
np.random.seed(42)  # For reproducibility

claims_id = [f"C{i:03}" for i in range(1, 51)]
cpt_codes = [f"CPT{i:03}" for i in range(1, 51)]
diagnoses = [f"Diag{i:03}" for i in range(1, 51)]
successful_prob = np.random.uniform(0.01, .9, 50)  # Random probabilities between 0.5 and 1.0
allowed_amount = np.random.randint(500, 2000, 50)  # Random amounts between 500 and 2000

# Create a DataFrame
data = {
    "Claims Id": claims_id,
    "CPT Code": cpt_codes,
    "Diagnosis": diagnoses,
    "Successful Adjudication Probability": successful_prob,
    "Allowed Amount": allowed_amount
}

df = pd.DataFrame(data)

# Calculating Expected Allowed Amount
df["Expected Allowed Amount"] = df["Successful Adjudication Probability"] * df["Allowed Amount"]

# Round columns to 0 decimal places
df["Successful Adjudication Probability"] = df["Successful Adjudication Probability"].round(2)
df["Allowed Amount"] = df["Allowed Amount"].round(0)
df["Expected Allowed Amount"] = df["Expected Allowed Amount"].round(0)

# Streamlit App Layout
st.title("Claims Adjudication Probability Dashboard")

# Add sort options
sort_by = st.selectbox(
    "Sort By", 
    options=["Allowed Amount", "Expected Allowed Amount"],
    index=0  # Default to "Allowed Amount"
)

# Sort the DataFrame based on the user's selection
if sort_by == "Allowed Amount":
    df = df.sort_values(by="Allowed Amount", ascending=False)
else:
    df = df.sort_values(by="Expected Allowed Amount", ascending=False)

# Display DataFrame
st.write("Claims Data with Expected Allowed Amount (50 rows):")
st.dataframe(df)
