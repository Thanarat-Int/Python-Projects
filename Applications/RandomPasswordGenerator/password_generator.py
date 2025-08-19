import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

def generate_password():
    try:
        length = int(length_entry.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for length.")
        return

    use_upper = upper_var.get()
    use_digits = digits_var.get()
    use_special = special_var.get()

    characters = string.ascii_lowercase
    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        messagebox.showwarning("No Options", "Please select at least one character set.")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def copy_password():
    password = password_entry.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied to clipboard.")
    else:
        messagebox.showwarning("Empty", "No password to copy.")

# GUI Setup
root = tk.Tk()
root.title("🔐 Password Generator")
root.geometry("400x300")
root.resizable(False, False)

tk.Label(root, text="Password Length:").pack(pady=5)
length_entry = tk.Entry(root, width=10, justify="center")
length_entry.pack()

upper_var = tk.BooleanVar()
digits_var = tk.BooleanVar()
special_var = tk.BooleanVar()

tk.Checkbutton(root, text="Include Uppercase Letters", variable=upper_var).pack()
tk.Checkbutton(root, text="Include Digits", variable=digits_var).pack()
tk.Checkbutton(root, text="Include Special Characters", variable=special_var).pack()

tk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)

password_entry = tk.Entry(root, width=40, justify="center")
password_entry.pack()

tk.Button(root, text="Copy to Clipboard", command=copy_password).pack(pady=10)

root.mainloop()
