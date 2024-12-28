import random
import string
def generate_password(pas_ln):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password="".join(random.choices(all_characters,k=pas_ln))    
    return password
def generate_password_conditions(pas_ln):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    pd=[random.choice(string.ascii_uppercase),random.choice(string.ascii_lowercase),random.choice(string.digits),random.choice(string.punctuation)]
    password="".join(random.choices(all_characters,k=pas_ln))    
    return password
pwd=int(input("Enter the length of password here:"))
password = generate_password_conditions(pwd)
print(password)
