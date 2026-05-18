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
    
    
    quarter = ["Q1", "Q2", "Q3", "Q4"]
    
    button = st.button ("Regenerate")
    if button:
        data = []
        sales = np.random.randint(50000,200000, 4)
        data.append({"Quarter": quarter, "Sales": sales})
        df = pd.DataFrame({"Quarter": quarter, "Sales": sales})
    
        barchart = st.bar_chart(df[["Quarter", "Sales"]].set_index("Quarter"))

        with open ("quarterly_sales.csv", "w") as file:
            writer = csv.DictWriter(file, fieldnames = ["Quarter", "Sales"])
            writer.writeheader()
            writer.writerows(data)
    
        with open ("quarterly_sales.csv", "r") as file:
            reader = csv.DictReader(file)

elif option == "Exercise 3":
    st.title("From CSV")
    
    products = '''Product,Category,Units_Sold,Price,Revenue
    Pro A,Electronics,245,150,36750
    Pro B,Clothing,890,45,40050
    Pro C,Electronics,320,200,64000
    Pro D,Home,156,80,12480
    Pro E,Clothing,540,60,32400
    Pro F,Electronics,410,120,49200
    Pro G,Home,278,55,15290
    Pro H,Clothing,670,50,33500
    Pro I,Electronics,195,300,58500
    Pro J,Home,430,40,17200'''
    
    with open ("products.csv", "w") as file:
        file.write(products)
        
    data = pd.read_csv("products.csv")
    st.dataframe(data)

    category = st.multiselect("Choose one or more category", ["Electronics", "Clothing", "Home"])
    filtered = data[data["Category"].isin(category)]
    
    st.bar_chart(filtered[["Category", "Units_Sold"]].set_index("Category"))
    

    st.scatter_chart(data[["Units_Sold", "Revenue"]].set_index("Units_Sold"), x_label= "Units Sold", y_label="Revenue")

    st.title("Generated from random")
    
    Price = np.random.randint(100,1000, 10)
    Revenue = np.random.randint(10,90, 10)
    df = pd.DataFrame({"Year": [2010,2011,2012,2013,2014,2015,2016,2017,2018,2019],
                  "Price": Price,
                  "Revenue": Revenue})
    st.dataframe(df)

    st.line_chart(df.set_index("Year"))
    revenue_data = list(df)
    cum = sum(int(revenue_data["Revenue"]))
    st.metric("Cumulative sum", f"${cum:,.2f}M")
    

    

    
        
            
    
    
    
    
    
    
            
                   








