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
password=generate_password_conditions(pwd)
print("Password Generated:",password)
import hashlib
data=password
hash_obj1=hashlib.sha256(data.encode())
hex_str1=hash_obj1.hexdigest()
print(hex_str1)
hash_obj2=hashlib.md5(data.encode())
hex_str2=hash_obj2.hexdigest()
print(hex_str2)
print(f"After applying SHA256:{hex_str1}")
print(f"After applying MD5:{hex_str2}")
print(f"Length of SHA256 hashing:{len(hex_str1)}")
print(f"Length of MD5 hashing:{len(hex_str2)}")
if (len(hex_str1)) > (len(hex_str2)):
    print("SHA256 is stronger than MD5")
else:
    print("MD5 is stronger than SHA256")