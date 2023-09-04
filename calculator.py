import re
import tkinter as tk

def calculate(expression):
    try:
        expression = re.sub(r'[^0-9+\-*/() ]', '', expression)
        result = eval(expression)
        return result
    except Exception as e:
        return "Error: " + str(e)

def calculate_button_click():
    user_input = entry.get()
    result = calculate(user_input)
    result_label.config(text="Result: " + str(result))

def clear_button_click():
    entry.delete(0, tk.END)
    result_label.config(text="Result:")

def main():
    root = tk.Tk()
    root.title("Python Calculator")

    frame = tk.Frame(root)
    frame.pack(padx=10, pady=10)

    entry = tk.Entry(frame)
    entry.pack(fill=tk.X)

    calculate_button = tk.Button(frame, text="Calculate", command=calculate_button_click)
    calculate_button.pack()

    clear_button = tk.Button(frame, text="Clear", command=clear_button_click)
    clear_button.pack()

    result_label = tk.Label(frame, text="Result:")
    result_label.pack()

    quit_button = tk.Button(frame, text="Quit", command=root.quit)
    quit_button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
