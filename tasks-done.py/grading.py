# Prompt the user to enter marks
marks = int(input("Enter student marks (0-100): "))

# Determine the grade based on marks
if marks > 79:
    grade = "A"
elif 60 <= marks <= 79:
    grade = "B"
elif 50 <= marks <= 59:
    grade = "C"
elif 40 <= marks <= 49:
    grade = "D"
else:
    grade = "E"

print("The grade is:", grade)
