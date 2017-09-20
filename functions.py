# defining a function

def hi():
    print("Hey, hey, heeeeey")
hi()

# return

def hi():
    return "Hey, hey, heeeeey"
print(hi())

# since we're returning a string, we can chain methods to it
print(hi().upper()) # uppercase

# customizing the return, parameters and .format
def hi(name):
    return 'Hi, {}'.format(name)
print(hi('Michael'))

# default parameter
def hi(greeting, name='You'):
    return '{}, {}'.format(greeting, name)
print(hi('Hello'))
print(hi('Hello', name = 'George'))

# *args and **kwargs
def person_info(*args, **kwargs):
    print(args) # tuple
    print(kwargs) #dictionary

person_info('Tall', 'Slim', name = "Toni", age = 27)

# or
description = ['Tall', 'Slim']
info = {'name': 'Toni', 'age': 27}
person_info(*description, **info) # the stars unpack the information, without them...

person_info(description, info)
