import streamlit as st
import math

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
                           ["Square Root", "Power", "Sin", "Cos", "Tan" "Log"])
    if option2 == "Square Root":
        try:
            st.success(f"Result: {sqrt(a)}")
        except ZeroDivisionError:
            st.write("You cannot take a square root of 0")

    elif option2 == "Power":
        st.success(f"Result: {a**b}")
        
    elif option2 == "Sin":
        try:
            st.success(f"Result: {sin(a)}")
        except ZeroDivisionError:
            st.write("Invalid input")
    
    elif option2 == "Cos":
        try:
            st.success(f"Result: {cos(a)}")
        except ZeroDivisionError:
            st.write("Invalid input")
    
    elif option2 == "Tan":
        try:
            st.success(f"Result: {tan(a)}")
        except ZeroDivisionError:
            st.write("Invalid input")

    else:
        try:
            st.success(f"Result: {log(a)}")
        except ZeroDivisionError:
            st.write("Invalid input")


