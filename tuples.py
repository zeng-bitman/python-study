#simple tuple
marks =(100,200,300,400,500,600)
print(marks)
print(type(marks))



#convert tuple to list
#modify
#revert back to tuple
marks =list(marks)
print(type(marks))  #converts to list

#all list modifications are possible
marks[3]= 2000  #example for mods possible
print(marks)

#converting back to tuple
marks=tuple(marks)
print(marks)


days =("monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday") #displays day of week
print(days[2])
print(days[-1])


#find length of tuple
print(len(days))
 

#replace thursday to thur
days=list(days) #converts

#replacing
days[3]="thur"

#reverts to tuple
days=tuple(days)
print(days)

