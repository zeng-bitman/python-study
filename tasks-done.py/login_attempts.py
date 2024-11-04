# Set correct email and password
correct_email = "bitman@gmail.com"
correct_password = "123456@7"

# Allow up to 3 attempts
for attempt in range(3):
    # Prompt for email and password
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    # Check if credentials match
    if email == correct_email and password == correct_password:
        print("Login is Successful")
        break
    else:
        print("Invalid username or password")

    # If three attempts have been used, block the user
    if attempt == 2:
        print("You have been blocked.")
