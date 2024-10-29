#dislay 1 to 50 inside a list
numbers = list(range(1, 51))
print(numbers)

#Display numbers divisible by 7 or 5 from the above list
divisible_by_7_or_5 = [num for num in numbers if num % 7 == 0 or num % 5 == 0]
print(divisible_by_7_or_5)

#3. Find sum and average of values in the range between 10 to 40
values = list(range(10, 41))
total_sum = sum(values)
average = total_sum / len(values)

print(f"Sum: {total_sum}, Average: {average}")

#4. Put the first 10 odd numbers between 10 and 50 inside a list
odd_numbers = [num for num in range(11, 51, 2)][:10]
print(odd_numbers)

#5. Multiplication table for a given number
number = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")


#6. Count and print the number of even numbers between 1 and 50
even_count = sum(1 for num in range(1, 51) if num % 2 == 0)
print(f"Number of even numbers between 1 and 50: {even_count}")

#7. Display the total quantity from the given list of tuples
ls1 = [("Jay", 20), ("Mo", 30), ("Mya", 32)]
total_quantity = sum(quantity for name, quantity in ls1)
print(f"Total quantity: {total_quantity}")
