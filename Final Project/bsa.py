import hashlib
accounts_db = {}
def add_account(username, password, account_no, balance):
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    accounts_db[username] = {
        'password_hash':password_hash,
        'account_no':account_no,
        'balance':balance
    }
    print(f"Account for {username} added successfully.")
def view_account(username):
    if username in accounts_db:
        account_info = accounts_db[username]
        print(f"\nAccount Info for{username}:")
        print(f"Account No:{account_info['account_no']}")
        print(f"Balance:${account_info['balance']}")
    else:
        print("Account not found.")
def check_password_hashing(password):
    sha256_hash = hashlib.sha256(password.encode()).hexdigest()
    md5_hash = hashlib.md5(password.encode()).hexdigest()
    print(f"\nSHA256 Hash:{sha256_hash}")
    print(f"MD5 Hash: {md5_hash}")
    return sha256_hash, md5_hash
def login(username, password):
    if username in accounts_db:
        stored_password_hash=accounts_db[username]['password_hash']
        input_password_hash=hashlib.sha256(password.encode()).hexdigest()
        if stored_password_hash==input_password_hash:
            print(f"\nLogin successful! Welcome, {username}.")
            view_account(username)
        else:
            print("Incorrect password.")
    else:
        print("Username not found.")
def show_savings(username):
    if username in accounts_db:
        account_info=accounts_db[username]
        print(f"\nAccount Savings for{username}:${account_info['balance']}")
    else:
        print("Account not found.")
while True:
    print("\nBank Secure Application")
    print("1.Add Account")
    print("2.View Account")
    print("3.Check Password Hashing (SHA256/MD5)")
    print("4.Login")
    print("5.Show Account Savings")
    print("6.Exit")
    choice=input("Select an option:")
    if choice=="1":
        username=input("Enter username:")
        password=input("Enter password:")
        account_no=input("Enter account number:")
        balance=float(input("Enter your balance:"))
        add_account(username,password,account_no,balance)
    elif choice=="2":
        username=input("Enter username to view account:")
        view_account(username)
    elif choice=="3":
        password=input("Enter password to check hashing:")
        check_password_hashing(password)
    elif choice=="4":
        username=input("Enter username:")
        password=input("Enter password:")
        login(username,password)
    elif choice=="5":
        username=input("Enter username to show savings:")
        show_savings(username)
    elif choice=="6":
        print("***Thank you for choosing our Bank Secure Application***")
        break
    else:
        print("Your pressing the invalid option")
