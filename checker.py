import re

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

password = input("Enter a password to test: ")
check_password(password)
