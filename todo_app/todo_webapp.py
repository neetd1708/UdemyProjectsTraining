import streamlit as st
import functions


st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is for increasing productivity")

todos = functions.get_tasks()


for task in todos:
    st.checkbox(task)

st.text_input(label="something",placeholder = "Enter a task...")


print("Hello")
