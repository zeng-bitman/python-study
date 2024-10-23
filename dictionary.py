person={
    'name':'jesse',
    'age':23,
    'gender':'male',
    'location':['embakasi', 100200, 'Nairobi'],
    'address':{
        'street':'moi drive road',
        'city':'Nairobi',
        'country':'Kenya',
    }
}
print(type(person))


print(person['name'])
print(person['age'])
print(person['gender'])
print(person['location'])


#only siplay 100200
print(person['location'][1])

#only display nairobi
print(person['location'][2])


#only display embakasi
print(person['location'][0])


#displays part of address
print(person['address']['street'])
print(person['address']['city'])
print(person['address']['country'])

#adding peroperties
person['occupatioon']='doctor'
print(person)

#update values in dictionary
person['age']=40
print(person)

#update location
person['location']='bamburi'
print(person)

#add phone number
person['phone number']='0701989426'
print(person)


#methods in dictionary

#.keys() ==returns all keys belonging to that dictionary
print(person.keys())
#.values() ==returns all values belonging to that dictionary
print(person.values())
#.items() ==returns a list containing a tule of each  keys and a value
print(person.items())
#.pop ==removes property of a specified key
person.pop('address')
print(person)

#popitem() ==removes last item added to the dictionary
person.popitem()
print(person)

#clear
person.clear()
print(person)