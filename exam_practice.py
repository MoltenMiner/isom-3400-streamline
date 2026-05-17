import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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
