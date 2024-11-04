from datetime import datetime

# Prompt the user to enter their date of birth
dob_str = input("Enter your date of birth (YYYY-MM-DD): ")
dob = datetime.strptime(dob_str, "%Y-%m-%d")
today = datetime.today()

# Calculate age
age_years = today.year - dob.year
age_months = today.month - dob.month
age_days = today.day - dob.day

# Adjust for month and day borrow if necessary
if age_days < 0:
    age_days += 30
    age_months -= 1
if age_months < 0:
    age_months += 12
    age_years -= 1

print(f"Age: {age_years} years, {age_months} months, and {age_days} days.")
