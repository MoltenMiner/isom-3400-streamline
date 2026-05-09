import streamlit as st

st.title('Greeting')
st.write("I do not know what this app is about.")
name = st.text_input("What is the username?")
age = st.number_input("What is the age?", min_value=0, max_value=120)
color = st.selectbox("What is your fav colour?", ["Red", "Blue", "Green"])
button = st.button("Enter")
if button:
    st.success(f"Thank you! Name: {name}, Age: {age}, Favourite Colour: {color}")
