import streamlit as st
st.title("Hello")
st.header("Isom 3400")
st.write("I am studying Isom 3400")
st.write("**Bold Text** and *Italic Text*")

age = st.number_input("Enter your age:",
                      min_value=0,
                      max_value=120,
                      value=25)  #Default value is 25
st.write(f"Your age is {age}")
