# Prompt the user to enter a number
number = int(input("Enter a number: "))

# Check if the number is even or odd
if number % 2 == 0:
    print("even")
    # Check if the number is divisible by 4
    if number % 4 == 0:
        print("divisible by 4")
else:
    print("odd")