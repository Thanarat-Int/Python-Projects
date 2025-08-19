import json
import datetime

def load_birthdays(filename="birthdays.json"):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_birthdays(birthdays, filename="birthdays.json"):
    with open(filename, "w") as f:
        json.dump(birthdays, f, indent=4)

def add_birthday(name, date_str):
    birthdays = load_birthdays()
    birthdays[name] = date_str
    save_birthdays(birthdays)
    print(f"🎉 เพิ่มวันเกิดของ {name} สำเร็จ")

def check_today_birthdays():
    today = datetime.date.today()
    today_str = today.strftime("%m-%d")
    birthdays = load_birthdays()
    found = False

    for name, date_str in birthdays.items():
        if date_str[5:] == today_str:
            print(f"🎈 วันนี้เป็นวันเกิดของ {name}!")
            found = True
    if not found:
        print("📅 วันนี้ไม่มีใครเกิดครับ")

def main():
    print("🎂 Birthday Reminder")
    print("[1] เช็ควันเกิดวันนี้")
    print("[2] เพิ่มวันเกิดใหม่")
    choice = input("เลือกเมนู: ")

    if choice == "1":
        check_today_birthdays()
    elif choice == "2":
        name = input("ใส่ชื่อ: ")
        date_str = input("ใส่วันเกิด (รูปแบบ YYYY-MM-DD): ")
        add_birthday(name, date_str)
    else:
        print("❌ เลือกไม่ถูกต้อง")

if __name__ == "__main__":
    main()
