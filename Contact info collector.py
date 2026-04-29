import streamlit as st
import pandas as pd
import numpy as np
import csv

with st.form(key="my_form"):

  First_name = st.text_input("What is your first name?")
  Last_name = st.text_input("What is your last name?")
  Fav_no = st.number_input("What is your favourite number?")
  button = st.form_submit_button("Register")
  if button:
    if First_name.strip != "" and Last_name.strip != "":
      
      
      contacts = pd.DataFrame({"First name": First_name, "Last name": Last_name})
      
    
