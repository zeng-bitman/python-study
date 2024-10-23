#we create a list of fruits
fruits =['grapes','peaches','banana','watermelon','ford','apple','avocado','oranges']
print(type(fruits))
print(fruits[3])
print(fruits[-1])
print(fruits[-2])

#adding to the list
fruits.append("something")   #adds another fruit in the end of list
print(fruits)
#insert to list
fruits.insert(2,"guess") #inserts another fruit in specific index in list
print(fruits)

#remove from list
fruits.remove("ford")
print(fruits)

#pop (removes item)+(first item in list)
fruits.pop(0)
print(fruits)


#make a list for days in a week
days= ['monday',[10,20,[100,200],30,['a','b'],40],'tuesday','wednesday','thursday','friday','saturday','sunday']
print(days[1][2][1])
print (days[1][4][1])

#modify
days[0]="monday"
print(days)


#slicing of sub set mostly right side []
numbers =[111223,20,3,44000,5746,644554,7,800878]
print(numbers[0:3])