def get_number(prompt):
    while True:
        value = input(prompt)
        if value.replace('.', '', 1).isdigit():
            return float(value)
        print("Invalid character entered. Please enter a valid number.")

num1 = get_number("Enter the first number: ")
num2 = get_number("Enter the second number: ")
print(f"The sum of {num1} and {num2} is: {num1 + num2}")
