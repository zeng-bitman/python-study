# Prompt the user to enter a phone number
phone_number = input("Enter your phone number: ")

# Check and convert to standard format starting with +254
if phone_number.startswith("07"):
    phone_number = "+254" + phone_number[1:]
elif phone_number.startswith("01"):
    phone_number = "+254" + phone_number[1:]
elif phone_number.startswith("254"):
    phone_number = "+" + phone_number
elif phone_number.startswith("1"):
    phone_number = "+254" + phone_number
elif phone_number.startswith("+254"):
    # Already in correct format
    pass
else:
    print("Invalid phone number format.")
    
print("Formatted phone number:", phone_number)