import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv

'''
Task 4 – Bar Chart with Product Filter (5 points)
Add a st.selectbox() that lets the user choose a single product (A, B, or C).
When a product is selected, display a bar chart showing Sales for that product only, grouped by Region.
Use st.bar_chart().
Task 5 – Scatter Plot (3 points)
Create a scatter plot with Units on the x‑axis and Sales on the y‑axis.
Color the points by Region (you may use st.scatter_chart() with a properly formatted DataFrame, or use matplotlib/altair if needed – but st.scatter_chart is acceptable).
Hint: st.scatter_chart accepts a DataFrame with columns x, y, and optionally color.
Task 6 – CSV Export of Filtered Data (3 points)
Add a st.button() labeled "Export Filtered Data".
When clicked, the app should save the currently filtered data (based on the selected product from Task 4) to a new CSV file named filtered_data.csv.
Display a success message using st.success() when the export is complete.'''

st.set_page_config(page_title = "Sales Performance Dashboard")
st.title("Sales Performance Dashboard")

sales_data = '''Date,Product,Region,Sales,Units
2024-01-01,A,North,1200,15
2024-01-02,B,South,850,10
2024-01-03,A,East,2100,25
2024-01-04,C,West,950,8
2024-01-05,B,North,1750,20
2024-01-06,A,South,3200,40
2024-01-07,C,East,600,5
2024-01-08,B,West,1400,16
2024-01-09,A,North,980,12
2024-01-10,C,South,2500,30
'''

with open ("sales_data.csv", "w") as file:
    file.write(sales_data)

data = pd.read_csv("sales_data.csv")
col1, col2 = st.columns(2)
with col1:
    st.metric("Number of rows", data.shape[0])

with col2:
    st.metric("Number of columns", data.shape[1])
data = []
with open ("sales_data.csv", "r") as file:
    reader = csv.DictReader(file)
    for i in reader:
        data.append({"Date": i["Date"], "Sales": int(i["Sales"])})

st.line_chart(data[["Date", "Sales"]].set_index("Date"))


    
    



