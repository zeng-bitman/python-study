#enter an email address

email = input("Enter your email address: ")

# Check if the email contains "@" and "."
if "@" in email and "." in email:
    print("Valid email.")
else:
    print("Invalid email.")
