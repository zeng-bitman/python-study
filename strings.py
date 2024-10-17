first_name="zeng"
second_name="bitman"
print(first_name)
print(second_name)

#concatenation
full_name= first_name+ " " +second_name
print(full_name)

age="23"
print(age)

gender="male"
print(gender)

institution_name="TECH-CAMP"
print(institution_name)

school_fees="46000"
print(school_fees)

text ="python class for noobs"
print(text[8])
print(text[10])
print(text.index("n"))
print(text.index("noobs"))

text ="manchester united"
text =text.capitalize()
text2 =text.upper()
text3 =text.lower()


print(text)
print(text2)
print(text3)

email ="     badman@gmail.com"
v_email =email.strip()
print(email)
print(v_email)
text ="schools of crescent"
text =text.split(' ')
print(text)

text ="python class for beginners"
print(text[17:26])
print(text[13:16])
print(text[7:12])
print(text[0:6])

# displays print value for python class for beginners

text ="city is better than united"
text =text.replace('better','worse')
print(text)

email ="realbadman@gmail.com"
print(len(email))
print(email.count('@'))

#removing whitespaces
name ="   john doe   "
v_name =name.strip()
print(v_name)

#reverse a string
text ="reverse this"
print(text[:: -1])

#check substring presence (use count )
quote ="the best way to predict the future is to create on"
print(quote.count('future'))
print(quote.count('the'))
