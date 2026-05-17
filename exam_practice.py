import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu
import csv


with st.sidebar:
    option = option_menu(menu_title = "Menu",
                         options = ["Exercise 1", "Exercise 2", "Exercise 3", "Exercise 4", "Exercise 5"],
                         default_index = 0)
    
if option == "Exercise 1":
    st.title("Exercise 1")
    
    data = '''Month,Revenue,Expenses
    Jan,125000,85000
    Feb,118000,82000
    Mar,142000,91000
    Apr,137000,88000
    May,159000,94000
    Jun,168000,97000'''
    
    with open("sales_data.csv", "w") as file:
        file.write(data)
    
    df = pd.read_csv("sales_data.csv")
    
    
    st.dataframe(df)
    st.line_chart(df[["Month", "Revenue", "Expenses"]].set_index("Month"))

elif option == "Exercise 2":
    st.title("Exercise 2")
    
    sales = np.random.randint(50000,200000, 4)
    quarter = ["Q1", "Q2", "Q3", "Q4"]
    df = pd.DataFrame({"Quarter": quarter, "Sales": sales})
    st.bar_chart(df[["Quarter", "Sales"]].set_index("Quarter"))

    with open ("quarterly_sales.csv", "w") as file:
        writer = csv.DictWriter(file, fieldnames = ["Quarter", "Sales"])
        writer.writeheader()
        writer.writerows(df)
    
    with open ("quarterly_sales.csv", "r") as file:
        reader = csv.DictReader(file)
    
    
    button = st.button ("Regenerate")
    if button:
        sales = np.random.randint(50000,200000, 4)
        
        df = pd.DataFrame({"Quarter": quarter, "Sales": sales})
        with open ("quarterly_sales.csv", "w") as file:
            writer = csv.DictWriter(file, fieldnames = ["Quarter", "Sales"])
            writer.writeheader()
            writer.writerows(df)
    
        with open ("quarterly_sales.csv", "r") as file:
            reader = csv.DictReader(file)
    
        st.bar_chart(df[["Quarter", "Sales"]].set_index("Quarter"))
        
        
        






        
               








