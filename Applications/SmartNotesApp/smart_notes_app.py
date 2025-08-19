import tkinter as tk
from tkinter import messagebox, filedialog
import os
from datetime import datetime

NOTES_DIR = "notes"
os.makedirs(NOTES_DIR, exist_ok=True)

def save_note():
    title = title_entry.get().strip()
    content = text_area.get("1.0", tk.END).strip()

    if not title:
        messagebox.showwarning("Missing Title", "Please enter a note title.")
        return

    filename = f"{title}.txt"
    filepath = os.path.join(NOTES_DIR, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    messagebox.showinfo("Saved", f"Note saved as {filename}")
    refresh_note_list()

def load_note():
    selected = note_listbox.curselection()
    if not selected:
        return

    filename = note_listbox.get(selected[0])
    filepath = os.path.join(NOTES_DIR, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    title_entry.delete(0, tk.END)
    title_entry.insert(0, filename.replace(".txt", ""))
    text_area.delete("1.0", tk.END)
    text_area.insert(tk.END, content)

def refresh_note_list():
    note_listbox.delete(0, tk.END)
    for file in sorted(os.listdir(NOTES_DIR)):
        if file.endswith(".txt"):
            note_listbox.insert(tk.END, file)

def delete_note():
    selected = note_listbox.curselection()
    if not selected:
        return
    filename = note_listbox.get(selected[0])
    filepath = os.path.join(NOTES_DIR, filename)
    os.remove(filepath)
    refresh_note_list()
    title_entry.delete(0, tk.END)
    text_area.delete("1.0", tk.END)
    messagebox.showinfo("Deleted", f"{filename} has been deleted.")

# GUI setup
app = tk.Tk()
app.title("📝 Smart Notes App")
app.geometry("700x450")

# Left pane: Note list
left_frame = tk.Frame(app)
left_frame.pack(side="left", fill="y", padx=10, pady=10)

note_listbox = tk.Listbox(left_frame, width=30, height=20)
note_listbox.pack()
note_listbox.bind("<<ListboxSelect>>", lambda e: load_note())

btn_del = tk.Button(left_frame, text="🗑 Delete", command=delete_note, bg="#e74c3c", fg="white")
btn_del.pack(pady=5)

# Right pane: Editor
right_frame = tk.Frame(app)
right_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

title_entry = tk.Entry(right_frame, font=("Segoe UI", 12))
title_entry.pack(fill="x", pady=5)

text_area = tk.Text(right_frame, wrap="word", font=("Segoe UI", 11))
text_area.pack(fill="both", expand=True)

btn_save = tk.Button(right_frame, text="💾 Save Note", command=save_note, bg="#27ae60", fg="white")
btn_save.pack(pady=8)

refresh_note_list()
app.mainloop()
