import random
import string

length = int(input("Enter the length of the password: "))
lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
digits = input("Include digits? (y/n): ").lower() == 'y'
symbols = input("Include symbols? (y/n): ").lower() == 'y'

characters = ''
if lowercase:
    characters += string.ascii_lowercase
if uppercase:
    characters += string.ascii_uppercase
if digits:
    characters += string.digits
if symbols:
    characters += string.punctuation

password = ''.join(random.choice(characters) for _ in range(length))
print(f"Your password is: {password}")
