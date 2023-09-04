import tkinter as tk
import random
import string

def generate_password():
    length = int(length_entry.get())
    if length <= 0:
        password_result.set("Invalid length")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    password_result.set(password)

# Create the main window
root = tk.Tk()
root.title("Random Password Generator")

# Create and configure widgets
length_label = tk.Label(root, text="Password Length:")
length_label.pack()

length_entry = tk.Entry(root)
length_entry.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()

password_result = tk.StringVar()
password_label = tk.Label(root, textvariable=password_result)
password_label.pack()

# Start the Tkinter main loop
root.mainloop()
