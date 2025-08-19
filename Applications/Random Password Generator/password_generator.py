import random
import string
import pyperclip

def generate_password(length, use_upper, use_digits, use_special):
    characters = string.ascii_lowercase
    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        return None

    return ''.join(random.choice(characters) for _ in range(length))

def main():
    print("🔐 Random Password Generator")

    try:
        length = int(input("ความยาวของรหัสผ่าน: "))
    except ValueError:
        print("❌ ต้องเป็นตัวเลข")
        return

    use_upper = input("ใช้ตัวพิมพ์ใหญ่ด้วยไหม? (y/n): ").lower() == 'y'
    use_digits = input("ใช้ตัวเลขด้วยไหม? (y/n): ").lower() == 'y'
    use_special = input("ใช้สัญลักษณ์พิเศษด้วยไหม? (y/n): ").lower() == 'y'

    password = generate_password(length, use_upper, use_digits, use_special)

    if password:
        print(f"\n✅ รหัสผ่านของคุณคือ:\n{password}")
        pyperclip.copy(password)
        print("(📋 คัดลอกไปยังคลิปบอร์ดแล้ว)")
    else:
        print("❌ คุณไม่ได้เลือกอักขระใด ๆ เลย")

if __name__ == "__main__":
    main()
