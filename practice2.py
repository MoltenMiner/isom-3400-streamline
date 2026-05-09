import streamlit as st
import math
import pandas as pd
import time
from streamlit_option_menu import option_menu


st.title('Greeting')
st.write("I do not know what this app is about.")
name = st.text_input("What is the username?")
age = st.number_input("What is the age?", min_value=0, max_value=120)
color = st.selectbox("What is your fav colour?", ["Red", "Blue", "Green"])
button = st.button("Enter")
if button:
    st.success(f"Thank you! Name: {name}, Age: {age}, Favourite Colour: {color}")

#Calculator#

a = st.number_input("What is a?")
b = st.number_input("What is b?")

option = st.selectbox("What is the operation?", ["Add", "Subtract", "Multiply", "Divide", "Advanced"])
if option == "Add":
    st.success(f"Result: {a+b}")
elif option == "Subtract":
    st.success(f"Result: {a-b}")
elif option == "Multiply":
    st.success(f"Result: {a*b}")
elif option == "Divide":
    try:
        st.success(f"Result: {a/b}")
    except ZeroDivisionError:
        st.write("You cannot divide by 0")

else:
    option2 = st.selectbox("What is the advanced operation?", 
                           ["Square Root", "Power", "Sin", "Cos", "Tan", "Log"])
    if option2 == "Square Root":
        try:
            st.success(f"Result: {math.sqrt(a)}")
        except ZeroDivisionError:
            st.write("You cannot take a square root of 0")

    elif option2 == "Power":
        st.success(f"Result: {a**b}")
        
    elif option2 == "Sin":
        try:
            st.success(f"Result: {math.sin(a)}")
        except ZeroDivisionError:
            st.write("Invalid input")
    
    elif option2 == "Cos":
        try:
            st.success(f"Result: {math.cos(a)}")
        except ZeroDivisionError:
            st.write("Invalid input")
    
    elif option2 == "Tan":
        try:
            st.success(f"Result: {math.tan(a)}")
        except ZeroDivisionError:
            st.write("Invalid input")

    else:
        try:
            st.success(f"Result: {math.log(a)}")
        except ZeroDivisionError:
            st.write("Invalid input")

#streamlit_option_menu#
with st.sidebar:
    selected = option_menu(menu_title="Menu", 
                            options= ["Home", "About", "Contact", "Data Insights", "Business Performance Dashboard"],
                            default_index = 0)

if selected == "Home":
    st.title(f"Welcome to {selected}!")
    st.write ("Do you know human got 2 eyes?")
elif selected == "About":
    st.title(f"Welcome to {selected}!")
    st.write("About this app: IDK")
    st.write("App developer: me")
elif selected == "Contact":
    st.title(f"Welcome to {selected}!")
    with st.form(key= "Email"):
        st.text_input("Enter your email:")
        button = st.form_submit_button("Register")
        if button:
            st.success("Success!")
        
elif selected == "Data Insights":
    st.title(f"Welcome to {selected}!")
    data = st.file_uploader("Upload your csv here", type="csv")
    df = pd.read_csv(data)

    st.dataframe(df.head(10))
#Business dashboard
elif selected == "Business Performance Dashboard":
    st.title("Business Performance Dashboard")
    col1, col2,col3 = st.columns(3)

    with col1:
        st.header("Q1")
        st.write("$1.2M")
    with col2:
        st.header("Q2")
        st.write("$1.5M")
    with col3:
        st.header("Q3")
        st.write("$1.3M")

    tab1, tab2, tab3 = st.tabs(["Sales Data", "Customer Insights" , "Market Trends"])
    with tab1:
        data = pd.DataFrame({"Quarter": [1,2,3,4], "Revenue": [1.2,1.5,1.3,2]})
        st.dataframe(data)
    with tab2:
        comments = ["I love choco!", "I hate choco!", "IDK"]
        for i in comments:
            st.write(i)

    with tab3:
        status = {"Eco-friendly": "increasing", 
              "DEI": "decreasing", 
              "Choco": "no change"}
        for key, value in status.items():
            st.write(f"{key}: {value}")
        with st.expander('More information'):
            st.write("Data collected from nowhere")
    box = st.empty()
    for i in range(5):
        box.write(f"Loading {i*20}...")
        time.sleep(1)

    box.write("Business insights: IDK")
    quarter = st.selectbox("Quarter", ["Q1", "Q2", "Q3", "Q4"])
    growth = st.slider("Growth", min_value = 0, max_value = 100)
    rev_map = {"Q1": 1.2, "Q2": 1.5, "Q3": 1.3, "Q4": 1.6}
    rev = rev_map[quarter]*(1+growth/100)
    st.write(quarter, rev_map[quarter], rev)

    st.bar_chart(rev_map, x= quarter, y = rev_map.values)
    
        
        
    

























