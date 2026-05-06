import streamlit as st
import functions

todos = functions.get_tasks()
print(["Checkpoint1"] + todos)
def add_todo():
    todo=st.session_state["new_todo"] + "\n"
    todos.append(todo)
    print(["Checkpoint2"] + todos)
    functions.add_task(todos)

st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is for increasing productivity")


for index, task in enumerate(todos):
    checkbox = st.checkbox(task, key=task)
    if checkbox:
        todos.pop(index)
        functions.add_task(todos)
        del st.session_state[task]
        st.rerun()

st.text_input(label="Add a New task",placeholder = "Enter a task...",
              on_change=add_todo,key='new_todo')


print("Exit Checkpoint")
