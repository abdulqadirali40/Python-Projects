# todos = []

# num_todo = int(input("How many todos you want to add: "))

# for a in range(1, num_todo+1):
#     add_todo = input(f"Add todo {a}: ")
#     todos.append(add_todo)

# print(f"Your todos: {todos}")

# while True:
#     choices = int(input("1. Add\n2. Delete\n3. View\n4. Exit"))

#     if choices == 1:
#         num_todo = int(input("How many todos you want to add: "))

#         for a in range(1, num_todo+1):
#             add_todo = input(f"Add todo {a}: ")
#             todos.append(add_todo)
    
#     elif choices == 2:
#         delete_todo = input("Which todo you want to delete: ")

#         if delete_todo in todos:
#             todos.remove(delete_todo)
#         else:
#             print(f"Todo {delete_todo} is not exist!")
    
#     elif choices == 3:
#         print(f"Your todos: {todos}")
    
#     elif choices == 4:
#         break
import tkinter as tk
from tkinter import simpledialog, messagebox

# Initialize main window
root = tk.Tk()
root.title("Todo App")
root.geometry("500x500")

todos = []

# Function to add todos
def add_todo():
    num = simpledialog.askinteger("Add Todos", "How many todos you want to add?")
    if num is None:
        return
    for i in range(1, num + 1):
        task = simpledialog.askstring("Add Todo", f"Enter todo {i}:")
        if task:
            todos.append(task)
    update_listbox()

# Function to delete todo
def delete_todo():
    selected = listbox.curselection()
    if not selected:
        messagebox.showwarning("Delete Todo", "Please select a todo to delete.")
        return
    for i in selected[::-1]:  # Delete in reverse to avoid index shift
        todos.pop(i)
    update_listbox()

# Function to update the listbox view
def update_listbox():
    listbox.delete(0, tk.END)
    for todo in todos:
        listbox.insert(tk.END, todo)

# Function to exit app
def exit_app():
    root.quit()

# Buttons
add_btn = tk.Button(root, text="Add Todo", font=("Arial", 15), width=10, command=add_todo)
add_btn.pack(pady=10)

delete_btn = tk.Button(root, text="Delete Selected Todo", font=("Arial", 15), width=20, command=delete_todo)
delete_btn.pack(pady=10)

exit_btn = tk.Button(root, text="Exit", font=("Arial", 15), width=10, command=exit_app)
exit_btn.pack(pady=10)

# Listbox to show todos
listbox = tk.Listbox(root, font=("Arial", 15), selectmode=tk.MULTIPLE, width=40, height=15)
listbox.pack(pady=20)

# Start the GUI
root.mainloop()
