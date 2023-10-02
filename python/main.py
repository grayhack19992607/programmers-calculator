import tkinter as tk
from tkinter import messagebox
from function import *

# Create a function to handle the button click event
def calculate():
    try:
        num = float(entry_num.get())
        num2 = float(entry_num2.get())
    except ValueError:
        messagebox.showerror("Error", "Invalid input: Please enter valid numbers")
        return

    operation = operation_var.get()

    if operation == "Add":
        res = addNum(num, num2)
    elif operation == "Subtract":
        res = subtractNum(num, num2)
    elif operation == "Multiply":
        res = multiNum(num, num2)
    elif operation == "Division":
        if num2 == 0:
            messagebox.showerror("Error", "Division by zero is not allowed")
            return
        res = divNum(num, num2)
    elif operation == "Modulus":
        if num2 == 0:
            messagebox.showerror("Error", "Modulus by zero is not allowed")
            return
        res = modNum(num, num2)
    else:
        messagebox.showerror("Error", "Invalid operation")
        return

    label_result.config(text=f"Result: {res}")

# Create the main window
window = tk.Tk()
window.title("Basic Programmer Calculator")

# Create input fields
label_num = tk.Label(window, text="Enter the first number:")
entry_num = tk.Entry(window)
label_num2 = tk.Label(window, text="Enter the second number:")
entry_num2 = tk.Entry(window)

# Create a dropdown menu for selecting the operation
operation_var = tk.StringVar()
operation_var.set("Add")  # Default operation is addition
operation_menu = tk.OptionMenu(window, operation_var, "Add", "Subtract", "Multiply", "Division", "Modulus")

# Create a button to perform the calculation
calculate_button = tk.Button(window, text="Calculate", command=calculate)

# Create a label to display the result
label_result = tk.Label(window, text="Result:")

# Arrange the widgets using the grid layout
label_num.grid(row=0, column=0)
entry_num.grid(row=0, column=1)
label_num2.grid(row=1, column=0)
entry_num2.grid(row=1, column=1)
operation_menu.grid(row=2, column=0, columnspan=2)
calculate_button.grid(row=3, column=0, columnspan=2)
label_result.grid(row=4, column=0, columnspan=2)

# Start the GUI event loop
window.mainloop()
