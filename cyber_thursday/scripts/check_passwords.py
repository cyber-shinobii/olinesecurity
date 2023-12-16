# Cyber Thursday Basic Python Script
# You'll need a file with passwords 

def analyze_passwords(passwords):
    weak_passwords = ["password", "123456", "qwerty", "admin", "letmein"]

    print("Analyzing passwords...")
    for password in passwords:
        if password in weak_passwords:
            print(f"Weak password detected: {password}")
        else:
            print(f"Strong password: {password}")

def read_passwords_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            passwords = [line.strip() for line in file.readlines()]
        return passwords
    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
        return

def main():
    # Get input file path from the user
    file_path = input("Enter the path to the file containing passwords: ")

    # Read passwords from the file
    passwords = read_passwords_from_file(file_path)

    # Analyze the passwords
    if passwords:
        analyze_passwords(passwords)
    else:
        print("No passwords to analyze. Exiting.")