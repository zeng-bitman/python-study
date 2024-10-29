# Nested if statement program to check transaction limits

# Taking input from the user
amount = float(input("Enter the transaction amount: "))
account_type = input("Enter account type (standard or premium): ").strip().capitalize()

# Checking the account type
if account_type == "standard":
    if amount > 500:
        print("Transaction exceeds the limit for standard accounts.")
    else:
        print("Transaction approved.")
elif account_type == "premium":
    if amount > 1000:
        print("Transaction exceeds the limit for premium accounts.")
    else:
        print("Transaction approved.")
else:
    print("Invalid account type. Please enter 'Standard' or 'premium'.")
