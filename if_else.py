
city = 'Minneapolis'
city = 'Chicago'

if city == 'Minneapolis':
    print('Best City EVER');
else:
    print('Not that cool');

# elif, able to add many elif statements

if city == 'Minneapolis':
    print('Best City EVER');
elif city == 'Chicago':
    print('I like Chicago too');
else:
    print('City Not Found');

# and

car = 'bmw'
driving = True
if car == 'bmw' and driving:
    print('VROOM VROOM')
else:
    print('Meh')

# or, not
# not changes boolean to its opposite
driving = False
if not driving:
    print('Not Driving')

# is
a = ['1','2','3']
b = ['1','2','3']

print(a == b) #true
print(a is b) #false because its a different object in memory, dif id's

# Things that evaluate to false: None, 0, empty(), empty[], empty{}, empty''
