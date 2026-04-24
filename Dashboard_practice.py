import streamlit as st

st.title("Retail Business Dashboard")
st.header("Manager Input Section")
st.write("Please enter the monthly sales target and select the region.")


monthly_salary = st.number_input("Enter Monthly Sales Target (in USD):", min_value=0, max_value=9999999999, value=0)
region= st.selectbox("Choose your region:", ["East", "South", "West", "North"])

if st.button("Submit"):
  st.success("Button clicked!")
  st.write(f"Your salary is {monthly_salary}. You live in the {region} area.")
