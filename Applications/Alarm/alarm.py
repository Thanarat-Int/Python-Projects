import datetime
import time
from playsound import playsound

def get_alarm_time():
    while True:
        alarm_input = input("⏰ ตั้งเวลาปลุก (รูปแบบ HH:MM AM/PM): ").strip()
        try:
            alarm_time = datetime.datetime.strptime(alarm_input, "%I:%M %p")
            now = datetime.datetime.now()
            # รวมวันและเวลาปลุก
            alarm_time = now.replace(hour=alarm_time.hour, minute=alarm_time.minute, second=0, microsecond=0)
            # ถ้าตั้งเวลาแล้วเวลาผ่านไปแล้ว → เลื่อนเป็นวันถัดไป
            if alarm_time < now:
                alarm_time += datetime.timedelta(days=1)
            return alarm_time
        except ValueError:
            print("❌ รูปแบบไม่ถูกต้อง! กรุณาใช้ HH:MM AM/PM เช่น 07:30 AM")

def main():
    print("=== Python Alarm Clock ===")
    alarm_time = get_alarm_time()
    print(f"🔔 รอจนถึงเวลา {alarm_time.strftime('%I:%M %p')} เพื่อปลุก...")

    while True:
        now = datetime.datetime.now()
        if now >= alarm_time:
            print("🔊 ถึงเวลาปลุก! ตื่นได้แล้ว!")
            playsound("alarm_sound.mp3")
            break
        time.sleep(1)

if __name__ == "__main__":
    main()
