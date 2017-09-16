# keys and values
person = {'name': 'Antonio' , 'age': 27, 'occupation': 'developer' };
print(person);
print(person['name']);

# get method, returns 'none' instead of an error if property is undefined
print(person.get('phone'))

# update values
person['phone'] = '555-555-5555';
print(person.get('phone')); #will return none
print(person.get('phone', 'Not Found')); #will return not found instead of none


person['name'] = 'Rice';
print(person['name']); #will return rice

print(person);

# update multiple items in the dictionary
person.update({'name': 'John', 'phone': '612-222-2222'});
print(person);

# delete value
del person['age'];
print(person);

occupation = person.pop('occupation');
print('occupation');
print(person);

#length of keys in dictionary
print(len(person));
# view all keys
print(person.keys());
# values
print(person.values());

# loop through the dictionary, returning keys
for key in person:
    print(key);
# loop through the dictionary, returning keys and values
for key, value in person.items():
    print(key, value);
