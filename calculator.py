import tkinter as tk

def evaluate_expression():
    try:
        result.set(eval(entry.get()))
    except Exception as e:
        result.set("Error")

def clear_entry():
    entry.delete(0, tk.END)
    result.set("")

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create an Entry widget for user input
entry = tk.Entry(root, font=("Arial", 20))
entry.grid(row=0, column=0, columnspan=4)

# Create a StringVar to display the result
result = tk.StringVar()
result.set("")
result_label = tk.Label(root, textvariable=result, font=("Arial", 20))
result_label.grid(row=1, column=0, columnspan=4)

# Create buttons for numbers and operations
buttons = [
    '7', '8', '9', '+',
    '4', '5', '6', '-',
    '1', '2', '3', '*',
    '0', '.', '=', '/'
]

row_val, col_val = 2, 0

for button in buttons:
    tk.Button(root, text=button, padx=20, pady=20, font=("Arial", 20), command=lambda b=button: entry.insert(tk.END, b) if b != '=' else evaluate_expression()).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Create a clear button
tk.Button(root, text="Clear", padx=20, pady=20, font=("Arial", 20), command=clear_entry).grid(row=6, column=0, columnspan=4)

# Run the GUI
root.mainloop()
