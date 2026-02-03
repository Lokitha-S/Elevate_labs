import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email)

def validate_mobile(mobile):
    pattern = r'^[6-9]\d{9}$'
    return re.match(pattern, mobile)

def validate_password(password):
    pattern = r'^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    return re.match(pattern, password)

def run_validator():
    print("__________Input______________")
    
    email = input("Enter Email: ").strip()
    if validate_email(email):
        print("Valid Email")
    else:
        print("Invalid Email Format (e.g., user@example.com)")

    mobile = input("Enter Indian Mobile No: ").strip()
    if validate_mobile(mobile):
        print("Valid Mobile Number")
    else:
        print("Invalid Mobile (Must be 10 digits starting with 6-9)")

    print("\n[Password must be 8+ chars, with 1 Uppercase, 1 Digit, 1 Special Char]")
    pwd = input("Create Password: ").strip()
    if validate_password(pwd):
        print("Secure Password")
    else:
        print("Password does not meet security requirements")

if __name__ == "__main__":
    run_validator()