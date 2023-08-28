import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation 
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

password_length = int(input("Enter length of the password you want: "))
generated_password = generate_password(password_length)
print("The generated password is: ", generated_password)