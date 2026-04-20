import streamlit as st

st.title("Welcome to Streamlit!")

st.header("Section 1: Introduction")
st.write("Hello, Streamlit!")
st.write(12345)
st.write({"Name": "Alice", "Age": 30})

st.write(["list1", "list2"])

st.header("Section 2: Maarkdown")

st.write("**Bold Text** and *Italic Text*")

age = st.number_input("Enter your age:",
                      min_value=0,
                      max_value=120,
                      value=25)
st.write(f"Your age is {age}")
