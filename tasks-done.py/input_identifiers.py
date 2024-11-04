# Take four inputs from the user
nums = [int(input(f"Enter number {i+1}: ")) for i in range(4)]

# Find the maximum value
largest = max(nums)

# Display the largest number value
print(f"The largest number is: {largest}")
