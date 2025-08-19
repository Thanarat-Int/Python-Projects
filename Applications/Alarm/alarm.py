import tkinter as tk
from tkinter import messagebox
import datetime
import time
import threading
import pygame

# Initialize pygame for audio playback
pygame.init()

def set_alarm():
    alarm_time = time_entry.get()
    try:
        # รับเวลาในรูปแบบ HH:MM
        alarm_dt = datetime.datetime.strptime(alarm_time, "%H:%M")
        now = datetime.datetime.now()
        target = now.replace(hour=alarm_dt.hour, minute=alarm_dt.minute, second=0, microsecond=0)

        # ถ้าตั้งเวลาเป็นอดีต → เพิ่มเป็นวันถัดไป
        if target < now:
            target += datetime.timedelta(days=1)

        messagebox.showinfo("Alarm Set", f"Alarm set for {target.strftime('%I:%M %p')}")
        # สร้าง thread สำหรับรอเวลา
        threading.Thread(target=wait_and_ring, args=(target,), daemon=True).start()

    except ValueError:
        messagebox.showerror("Invalid Time", "Please enter time in HH:MM (24-hour format)")

def wait_and_ring(target_time):
    while datetime.datetime.now() < target_time:
        time.sleep(1)
    play_alarm()

def play_alarm():
    try:
        pygame.mixer.music.load("alarm_sound.mp3")
        pygame.mixer.music.play()
        messagebox.showinfo("⏰ Wake Up!", "It's time!")
    except Exception as e:
        messagebox.showerror("Error", f"Could not play alarm sound.\n{str(e)}")

# GUI layout
root = tk.Tk()
root.title("🔔 Alarm Clock")
root.geometry("300x200")
root.resizable(False, False)

tk.Label(root, text="Set Alarm Time (HH:MM):").pack(pady=10)

time_entry = tk.Entry(root, width=10, justify='center', font=("Arial", 14))
time_entry.pack()

tk.Button(root, text="Set Alarm", command=set_alarm).pack(pady=20)

root.mainloop()
