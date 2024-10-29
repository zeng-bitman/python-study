#it allows on to write a program that performs a task multiple times (multi times)
#allows to iterate through a sequence(list,tuples,strings,dictionary)
#types of loops
#for loops and while loop
#for loop
#iterates through a sequence

#syntax(for iterator_vas sequence:).....bloc of code
#eg
fruits= ['apple','mango','banana']

for fruits in fruits:
    if fruits =="banana":
        print(fruits)



#range ()==its used to create a list of numbers
#eg
x=list(range(10,40))
for numbers in x:
    print(x)

#iteration of 10 to 50 only with diplay of even numbers
even_number=[]
for number in range(10, 50):
    if number % 2 == 0:
        even_number.append(number)

print(even_number)