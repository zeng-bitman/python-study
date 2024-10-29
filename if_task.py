start_date = '2024-01-01'
end_date = '2024-12-31'

if start_date < end_date:
    print("Valid period")
elif start_date > end_date:
    print("Invalid period")
else:
    print("One-day period")

str1 = "Hello"
str2 = "World!"

if len(str1) > len(str2):
    print("str1 is longer")
elif len(str2) > len(str1):
    print("str2 is longer")
else:
    print("Both are of equal length")

#3
valid_ids = [101, 102, 103]
user_id = 101

if user_id in valid_ids:
    print("Access Granted")
else:
    print("Access Denied")



#4
value = "2000"
if type(value)==str:
    print("String Detected")
elif isinstance(value, int):
    print("Integer Detected")
else:
    print("Unknown Type")

#5
x = 7
y = 14

if x % 2 == 0:
    if y % 2 == 0:
        print("x and y are both even")
    else:
        print("Only x is even")
else:
    if y % 2 == 0:
        print("Only y is even")
    else:
        print("Neither x nor y are even")
