trainnes =["john", [2, ["james" , "mary"]]]
print(trainnes[1][0])   #displays 2 from list
print(trainnes[1][1][0])   #outputs james from list
trainnes.append(56)       #adds number 56 from list
print(trainnes)      #adds name mike between james and mary
trainnes[1][1].insert(1, 'mike')
print(trainnes)
trainnes[1][0]=8     #changes number 2 to 8
print(trainnes)


#remove john and mary
trainnes.remove('john') #removes john only
trainnes[0][1].remove('mary')
print(trainnes)

#determines length of list
print(len(trainnes))