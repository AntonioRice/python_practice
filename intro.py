# printing a string
print('Hello World');

# setting a variable to a string
message = "Bobbys World"

# returning the variable
print(message);

# returning lenth of string
print(len(message));

# returning index 0
print(message[0]);

# returning index 11
print(message[11]);

# slicing, only showing bobbys
print(message[0:6]);
print(message[:6]);

# only showing word
print(message[7:]);

# message to lowercase
print(message.lower());
# message to uppercase
print(message.upper());

# counting
print(message.count('b'));

# find, will return start index of 7
print(message.find('World'));

# replace word in string
message = message.replace('World', 'USA');
print(message);

# concat
greeting = 'Whats up';
name = 'Rice';

message = greeting + ', ' + name;
print(message);

# organizing concat with placeholders
message = '{}, {}. Welcome!'.format(greeting, name);
print(message);

# what methods are available
print(dir(message));

# what all the method does
print(help(str));

# specific info
print(help(str.lower));
