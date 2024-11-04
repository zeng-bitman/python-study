attempts = 4
correct_password = "techcamp2024"

for i in range(attempts):
    password = input("Enter your password: ")
    if password == correct_password:
        print("Access granted")
        break
    else:
        print("Incorrect password. Try again.")
else:
    print("Account blocked.")
