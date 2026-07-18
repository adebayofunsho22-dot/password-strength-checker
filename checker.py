import re
import random
import string

def check_password(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("❌ Add at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Add at least one lowercase letter.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("❌ Add at least one special character.")

    print("\n===== Password Strength Report =====")

    if score == 5:
        print("✅ Strength: Strong")
    elif score >= 3:
        print("🟡 Strength: Medium")
    else:
        print("🔴 Strength: Weak")

    print(f"Score: {score}/5")

    if feedback:
        print("\nSuggestions:")
        for item in feedback:
            print(item)
    else:
        print("\n🎉 Excellent password!")

def generate_password(length):
    characters = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )

    password = ''.join(random.choice(characters) for _ in range(length))

    print("\n===== Generated Password =====")
    print(password)

while True:
    print("\n========== Password Toolkit ==========")
    print("1. Check Password Strength")
    print("2. Generate Password")
    print("3. Exit")

    choice = input("\nChoose an option: ")

    if choice == "1":
        password = input("Enter a password: ")
        check_password(password)

    elif choice == "2":
        try:
            length = int(input("Password length: "))
            if length < 8:
                print("Password length should be at least 8.")
            else:
                generate_password(length)
        except ValueError:
            print("Please enter a valid number.")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")
