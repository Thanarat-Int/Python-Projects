import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.ttk import Button, Label, Frame, Style

# Supported file types and their target folders
FILE_TYPES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.xls', '.xlsx', '.ppt', '.pptx'],
    'Audio': ['.mp3', '.wav', '.aac'],
    'Videos': ['.mp4', '.mkv', '.avi'],
    'Archives': ['.zip', '.rar', '.tar', '.gz'],
    'Scripts': ['.py', '.js', '.html', '.css'],
}

def organize_files(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            _, ext = os.path.splitext(filename)
            for folder, extensions in FILE_TYPES.items():
                if ext.lower() in extensions:
                    target_dir = os.path.join(directory, folder)
                    os.makedirs(target_dir, exist_ok=True)
                    shutil.move(file_path, os.path.join(target_dir, filename))
                    break

def select_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        folder_var.set(folder_selected)

def run_organizer():
    directory = folder_var.get()
    if not os.path.isdir(directory):
        messagebox.showerror("Error", "Please select a valid directory")
        return
    organize_files(directory)
    messagebox.showinfo("Success", "Files organized successfully!")

# GUI Setup
app = tk.Tk()
app.title("🧹 Auto File Organizer")
app.geometry("500x260")
app.resizable(False, False)

style = Style()
style.configure('TFrame', background='#f7f7f7')
style.configure('TButton', font=('Segoe UI', 10))
style.configure('TLabel', background='#f7f7f7', font=('Segoe UI', 11))

frame = Frame(app, padding="20")
frame.pack(fill=tk.BOTH, expand=True)

Label(frame, text="📂 Select a folder to organize:").pack(anchor=tk.W, pady=(0, 8))
folder_var = tk.StringVar()
tk.Entry(frame, textvariable=folder_var, width=50).pack(pady=5)
Button(frame, text="Browse", command=select_folder).pack(pady=5)
Button(frame, text="Organize Files", command=run_organizer).pack(pady=15)

Label(frame, text="Supported file types:").pack(anchor=tk.W, pady=(15, 0))
types_label = tk.Label(frame, text=", ".join(FILE_TYPES.keys()), font=('Segoe UI', 9), fg="gray")
types_label.pack(anchor=tk.W)

app.mainloop()
