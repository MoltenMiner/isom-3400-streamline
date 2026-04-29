# Write your code below
import streamlit as st
import pandas as pd
import numpy as np
import csv

header = ["First name", "Last name", "Favourite number"]
with st.form(key="my_form"):

  First_name = st.text_input("What is your first name?")
  Last_name = st.text_input("What is your last name?")
  Fav_no = int(st.number_input("What is your favourite number?"))
  button = st.form_submit_button("Register")

  contacts_dict = [{"First name": First_name, 
                    "Last name": Last_name, 
                    "Favourite number": Fav_no}]
      
  with open ("contacts.csv", "w", newline = '') as file:
      writer = csv.DictWriter(file, fieldnames= header)
      writer.writeheader()
      writer.writerows(contacts_dict)
  
  if button:
    if First_name.strip != () and Last_name.strip != ():
      st.success("Successfully added to the file!")

      with open ("contacts.csv", "r") as file:
        writer = csv.DictReader(file)
    
        st.dataframe(writer)
    
    elif not First_name or not Last_name or First_name.strip == () or Last_name.strip == ():
      st.write("You still have not entered all the required items!")
