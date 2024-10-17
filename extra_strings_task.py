#strings
first_name="zeng"
second_name="bitman"
print(first_name)
print(second_name)

#concatenation
full_name= first_name+ " " +second_name
print(full_name)

#indexing
text ="python"
print(text[0])
print(text[5])


#slicing
text ="learning python is fun"
print(text[9:15])

#replacing strings
text ="hello world"
text =text.replace('world','python')
print(text)


#uppercase and lowercase strings
text ="python programming"
text =text.upper()
text2 =text.lower()

print(text)
print(text2)

#count
sentence ="This is a simple sentence"
print(len(sentence))
print(sentence.count('s'))

#string length
topic ="Data Science"
print(len(topic))


#removing whitespaces
name ="   john doe   "
v_name =name.strip()
print(v_name)

#reverse a string
text ="reverse this"
print(text[:: -1])


#check substring presence (use count )
quote ="the best way to predict the future is to create it"
print(quote.count('future'))
print(quote.count('the'))
print ("create" in quote)
