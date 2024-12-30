Final Project

Reference

student = []
while True:
    print("Student Management System")
    print("Add user press 1")
    print("view user press 2")
    print("view the array length press 3")
    print("Exist: press 4")
    choice = input("Enter Choice:")
    if choice == "1":
        username = input("Enter username:")
        password = input("Enter password:")
        student.append({'username':username,'password':password})
        print(f"Successfully added: {len(student)}")
    elif choi
elif choice == "2":
        print(student)
    elif choice == "3":
        print(len(student))
    elif choice == "4":
        print(f"Thank you, we are closing application")
        break

Bank Secure application
Module 1: account add - username, password, accountNo, account saving
Module 2: account view
module 3: password hashing (SHA256 MD)///
module 4: username and password login user information display
module 5: saving amount - 500