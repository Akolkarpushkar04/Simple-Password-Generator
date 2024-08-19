import random
import string

def create_password(length=8, use_lowercase=True, use_uppercase=True, use_digits=True, use_special_chars=True):
    char_set = ''
    if use_lowercase:
        char_set += string.ascii_lowercase
    if use_uppercase:
        char_set += string.ascii_uppercase
    if use_digits:
        char_set += string.digits
    if use_special_chars:
        char_set += string.punctuation

    if not char_set:
        raise ValueError("At least one character set must be selected.")

    password = ''.join(random.choice(char_set) for _ in range(length))
    
    return password
length = int(input("Enter the desired password length: "))
use_lowercase = input("Include lowercase letters? (yes/no): ").lower() == 'yes'
use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
use_digits = input("Include digits? (yes/no): ").lower() == 'yes'
use_special_chars = input("Include special characters? (yes/no): ").lower() == 'yes'

password = create_password(length, use_lowercase, use_uppercase, use_digits, use_special_chars)
print("Generated Password:", password)
