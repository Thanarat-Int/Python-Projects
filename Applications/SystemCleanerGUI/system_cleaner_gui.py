import tkinter as tk
from tkinter import messagebox
import os
import shutil
import tempfile

# ฟังก์ชันสำหรับล้างไฟล์

def clean_temp():
    temp = tempfile.gettempdir()
    try:
        for root, dirs, files in os.walk(temp):
            for f in files:
                try:
                    os.remove(os.path.join(root, f))
                except:
                    pass
        messagebox.showinfo("Success", "🧹 Temp files cleaned!")
    except Exception as e:
        messagebox.showerror("Error", str(e))


def clean_recycle_bin():
    try:
        result = os.system("powershell.exe Clear-RecycleBin -Force")
        if result == 0:
            messagebox.showinfo("Success", "🗑 Recycle Bin emptied!")
        else:
            raise Exception("Permission denied or PowerShell not available.")
    except Exception as e:
        messagebox.showerror("Error", str(e))


def clean_recent():
    recent_path = os.path.expanduser('~\\AppData\\Roaming\\Microsoft\\Windows\\Recent')
    try:
        for item in os.listdir(recent_path):
            try:
                os.remove(os.path.join(recent_path, item))
            except:
                pass
        messagebox.showinfo("Success", "📄 Recent files cleaned!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI
app = tk.Tk()
app.title("System Cleaner")
app.geometry("350x300")
app.resizable(False, False)

frame = tk.Frame(app)
frame.pack(pady=30)

tk.Label(app, text="🧼 System Cleaner Utility", font=("Segoe UI", 14)).pack(pady=10)

tk.Button(frame, text="🧹 Clean Temp Files", command=clean_temp, width=30, bg="#27ae60", fg="white").pack(pady=5)
tk.Button(frame, text="🗑 Empty Recycle Bin", command=clean_recycle_bin, width=30, bg="#e67e22", fg="white").pack(pady=5)
tk.Button(frame, text="📄 Clear Recent Files", command=clean_recent, width=30, bg="#2980b9", fg="white").pack(pady=5)

tk.Label(app, text="Built with Python & Tkinter", font=("Segoe UI", 9)).pack(side="bottom", pady=10)

app.mainloop()
