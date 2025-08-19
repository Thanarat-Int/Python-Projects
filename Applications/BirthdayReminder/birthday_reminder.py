import tkinter as tk
from tkinter import messagebox
import datetime
import json
import os

DATA_FILE = "birthdays.json"

def load_birthdays():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_birthdays(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_birthday():
    name = name_entry.get()
    date = date_entry.get()
    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
        birthdays = load_birthdays()
        birthdays[name] = date
        save_birthdays(birthdays)
        messagebox.showinfo("Success", f"Added birthday for {name}")
        name_entry.delete(0, tk.END)
        date_entry.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Error", "Date must be in YYYY-MM-DD format")

def check_birthdays():
    today = datetime.date.today().strftime("%m-%d")
    birthdays = load_birthdays()
    matches = [name for name, date in birthdays.items() if date[5:] == today]
    if matches:
        messagebox.showinfo("🎉 Today’s Birthdays", "\n".join(matches))
    else:
        messagebox.showinfo("No Birthdays", "📅 No birthdays today.")

# GUI setup
root = tk.Tk()
root.title("🎂 Birthday Reminder")
root.geometry("400x300")

tk.Label(root, text="Name:").pack()
name_entry = tk.Entry(root, width=30)
name_entry.pack()

tk.Label(root, text="Birthday (YYYY-MM-DD):").pack()
date_entry = tk.Entry(root, width=30)
date_entry.pack()

tk.Button(root, text="Add Birthday", command=add_birthday).pack(pady=10)
tk.Button(root, text="Check Today's Birthdays", command=check_birthdays).pack()

root.mainloop()
