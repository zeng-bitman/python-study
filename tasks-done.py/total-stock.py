# List of products with stock values as the last element in each sublist
prods = [['omo', '30kshs', '300'], ['milk', '50kshs', '200'], ['bread', '45kshs', '359'], ['coffee', '5kshs', '79']]

# Calculate the total stock by summing the last element in each sublist
total_stock = sum(int(prod[-1]) for prod in prods)

# Display the result
print(f"The total stock is: {total_stock}")
