# password_generator.py

import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    length = int(input("Enter the length for the password: "))
    generated_password = generate_password(length)
    print(f"Generated Password: {generated_password}")
