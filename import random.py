import random
import string
def generate_password(length):
    all_characters = string.ascii_lowercase
    password = ''.join(random.choice(all_characters) for i in range(length))
    return password
length = int(input("Enter the  password length: "))
password = generate_password(length)
print("Generated password:", password)
