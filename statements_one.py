#if statements

if 20>30:
    print("this is true")
    #nothing prints since this is false
else:
    print("this is false")
    #will ran with this full coding 

#   IF statement code block runs if the condition is true
# IF ELSE statement will run



#declare variable marks () chwck if marks are above 50 print pass otherwise print fail
marks=50.1
if marks>50:
    print('pass')
else:
    print('fail')   #this is a pass/fail example of if / else condition

#declare variable number the check if number is even otherwise print odd
#%==()
num=88
if num%2==0:
    print('even')
else:
    print('odd')



#if elif else statemnt(always last)
#used when with many conditions with differnt possible outcomes
#start with if>elif>else


#example of grading system
marks=int(input('enter marks:'))

if  marks>=80 and marks<=100:
    print('A')
elif marks>=70 and marks<80:
    print('B')
elif marks>=60 and marks<70:
    print('C')
elif marks>=50 and marks<60:
    print('D')
else:
    print('E')

#use input from content to check age if greater than 60 print you are old
# if age is 18 and above and less than 60 print you are a child

age=int(input("enter your age"))
if  age>=60:
    print("you are old")
elif age>18 and age<60:
    print("your are an adult")
else:
    print("you are a child")




age=int(input("enter your age"))
if age>18:
    licence=input('have a driving license (y/o):')
if licence=='yes':
    print('eligible')
else:
    print('not eligible')
    else:
    print('too young to drive')