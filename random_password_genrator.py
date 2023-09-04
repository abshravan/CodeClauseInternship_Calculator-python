import tkinter as tk
import random
import string

def generate_password():
    length = int(length_entry.get())
    if length <= 0:
        password_result.set("Invalid length")
        return

    characters = ""
    if use_letters.get():
        characters += string.ascii_letters
    if use_numbers.get():
        characters += string.digits
    if use_special_characters.get():
        characters += string.punctuation

    if not characters:
        password_result.set("Select at least one character type")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    password_result.set(password)

# Create the main window
root = tk.Tk()
root.title("Random Password Generator")


root.geometry("300x350")  # Set a fixed window size
root.configure(bg="white")  # Set the background color to white

# Create and configure widgets 
font_style = ('Helvetica', 12)

length_label = tk.Label(root, text="Password Length:", font=font_style, bg="white")
length_label.pack(pady=10)

length_entry = tk.Entry(root, font=font_style)
length_entry.pack(pady=5)

use_letters = tk.IntVar()
letters_checkbox = tk.Checkbutton(root, text="Letters (A-Z, a-z)", variable=use_letters, font=font_style, bg="white")
letters_checkbox.pack(pady=5)

use_numbers = tk.IntVar()
numbers_checkbox = tk.Checkbutton(root, text="Numbers (0-9)", variable=use_numbers, font=font_style, bg="white")
numbers_checkbox.pack(pady=5)

use_special_characters = tk.IntVar()
special_characters_checkbox = tk.Checkbutton(root, text="Special Characters (!@#$%^&*()_+)", variable=use_special_characters, font=font_style, bg="white")
special_characters_checkbox.pack(pady=5)

generate_button = tk.Button(root, text="Generate Password", command=generate_password, font=font_style, bg="blue", fg="white")
generate_button.pack(pady=10)

password_result = tk.StringVar()
password_label = tk.Label(root, textvariable=password_result, font=font_style, bg="white")
password_label.pack(pady=10)

# Start the Tkinter main loop
root.mainloop()
