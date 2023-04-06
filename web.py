import streamlit as lt

import functions

todos = functions.get_todos()

def add_todo():
    todo = lt.session_state["textdo"] + "\n"

    todos.append(todo)

    functions.write_todos(todos)



lt.title("My 1st Todo-App")

lt.write("dont get afraid for ANYTHING")

lt.text("How can u Explain about god..!")

lt.subheader("This is My First Web App..!")

for index,todo in enumerate(todos):
    check = lt.checkbox(todo,key=todo)
    if check:
        todos.pop(index)
        functions.write_todos(todos)
        del lt.session_state[todo]
        lt.experimental_rerun()

lt.text_input(label="",placeholder="Enter a todo", key="textdo",
              on_change=add_todo)