import tkinter as tk

# Function to update the expression in the entry widget
def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(value))

# Function to clear the entry widget
def button_clear():
    entry.delete(0, tk.END)

# Function to calculate the result
def button_equal():
    try:
        result = eval(entry.get())  # Evaluate the expression entered by the user
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create the main window
window = tk.Tk()
window.title("Simple Calculator👌")

# Create the entry widget for displaying expressions and results
entry = tk.Entry(window, width=25, font=("Arial", 14), borderwidth=5, relief="solid", justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Buttons layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
]

# Add buttons to the window
for (text, row, col) in buttons:
    if text == "=":
        button = tk.Button(window, text=text, width=5, height=2, font=("Arial", 14), command=button_equal)
    else:
        button = tk.Button(window, text=text, width=5, height=2, font=("Arial", 14), command=lambda value=text: button_click(value))
    button.grid(row=row, column=col)

# Create clear button
clear_button = tk.Button(window, text="C", width=5, height=2, font=("Arial", 14), command=button_clear)
clear_button.grid(row=5, column=0, columnspan=4)

# Run the application
window.mainloop()
