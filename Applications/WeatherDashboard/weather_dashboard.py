import tkinter as tk
from tkinter import messagebox
import requests
import os
from dotenv import load_dotenv
from PIL import ImageTk, Image
from io import BytesIO

load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")  # เก็บ API KEY ใน .env

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=en"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def show_weather():
    city = entry.get()
    data = get_weather(city)
    if data:
        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"].capitalize()
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]
        icon_code = data["weather"][0]["icon"]
        icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"
        icon_response = requests.get(icon_url)
        icon_data = Image.open(BytesIO(icon_response.content))
        icon_image = ImageTk.PhotoImage(icon_data)

        icon_label.configure(image=icon_image)
        icon_label.image = icon_image
        result.set(f"🌡 Temp: {temp}°C\n💧 Humidity: {humidity}%\n🌬 Wind: {wind} m/s\n🔎 {desc}")
    else:
        messagebox.showerror("Error", "City not found!")

# GUI
app = tk.Tk()
app.title("Weather Dashboard")
app.geometry("350x400")
app.resizable(False, False)

tk.Label(app, text="🌍 Enter City Name:", font=("Segoe UI", 12)).pack(pady=10)
entry = tk.Entry(app, font=("Segoe UI", 14), justify="center")
entry.pack(pady=5)

tk.Button(app, text="Get Weather", command=show_weather, font=("Segoe UI", 12), bg="#3498db", fg="white").pack(pady=10)

icon_label = tk.Label(app)
icon_label.pack()

result = tk.StringVar()
tk.Label(app, textvariable=result, font=("Segoe UI", 12), justify="center").pack()

app.mainloop()
