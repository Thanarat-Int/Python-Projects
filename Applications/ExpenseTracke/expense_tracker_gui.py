import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import datetime

# ========== DATABASE SETUP ==========
conn = sqlite3.connect("expenses.db")
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        category TEXT,
        description TEXT,
        amount REAL
    )
""")
conn.commit()

# ========== FUNCTIONS ==========

def add_expense():
    date = date_entry.get()
    category = category_entry.get()
    description = desc_entry.get()
    try:
        amount = float(amount_entry.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Amount must be a number.")
        return

    if not (date and category and description):
        messagebox.showerror("Missing Info", "Please fill all fields.")
        return

    cursor.execute("INSERT INTO expenses (date, category, description, amount) VALUES (?, ?, ?, ?)",
                   (date, category, description, amount))
    conn.commit()
    messagebox.showinfo("Success", "Expense added!")
    clear_fields()
    show_expenses()

def clear_fields():
    date_entry.delete(0, tk.END)
    category_entry.delete(0, tk.END)
    desc_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)

def show_expenses():
    for row in tree.get_children():
        tree.delete(row)

    cursor.execute("SELECT date, category, description, amount FROM expenses ORDER BY date DESC")
    for row in cursor.fetchall():
        tree.insert('', tk.END, values=row)

    cursor.execute("SELECT SUM(amount) FROM expenses")
    total = cursor.fetchone()[0]
    total_label.config(text=f"Total: ฿{total:.2f}" if total else "Total: ฿0.00")

# ========== GUI SETUP ==========
root = tk.Tk()
root.title("💰 Expense Tracker")
root.geometry("600x500")

# Input Frame
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

tk.Label(input_frame, text="Date (YYYY-MM-DD):").grid(row=0, column=0)
date_entry = tk.Entry(input_frame)
date_entry.insert(0, datetime.date.today().isoformat())
date_entry.grid(row=0, column=1)

tk.Label(input_frame, text="Category:").grid(row=1, column=0)
category_entry = tk.Entry(input_frame)
category_entry.grid(row=1, column=1)

tk.Label(input_frame, text="Description:").grid(row=2, column=0)
desc_entry = tk.Entry(input_frame)
desc_entry.grid(row=2, column=1)

tk.Label(input_frame, text="Amount (฿):").grid(row=3, column=0)
amount_entry = tk.Entry(input_frame)
amount_entry.grid(row=3, column=1)

tk.Button(input_frame, text="Add Expense", command=add_expense).grid(row=4, columnspan=2, pady=10)

# Treeview Table
tree = ttk.Treeview(root, columns=("Date", "Category", "Description", "Amount"), show="headings")
for col in ("Date", "Category", "Description", "Amount"):
    tree.heading(col, text=col)
tree.pack(fill=tk.BOTH, expand=True)

# Total Display
total_label = tk.Label(root, text="Total: ฿0.00", font=("Arial", 14))
total_label.pack(pady=5)

show_expenses()
root.mainloop()
