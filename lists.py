# creating a list (array)
shoes = ['Nikes', 'Adidas', 'Dock Martens', 'Jordans'];
# length of list
print(len(shoes));
# specific index
print(shoes[0]);
# get last value using negative index
print(shoes[-1]);
# starting point:stopping point (the last index is not incuded)
print(shoes[0:2]);

# adding to list
# added to end of list
shoes.append('Polos');
print(shoes);

# adding to beginning of list
shoes.insert(0, 'Sperrys');
# print(shoes);

# list wihin a list
# append, extend, insert
shoes_2 = ['mens', 'womens', 'kids'];
shoes.insert(0, shoes_2);
print(shoes);

# removing item
shoes.remove(shoes_2);
print(shoes);

# removing last value
# popped = shoes.pop()
# print(popped);
# print(shoes);

shoes.reverse();
print(shoes)

# alphabetical order
shoes.sort();
print(shoes);

# sorting
nums = [5, 3, 2, 1, 4]
nums.sort()
print(nums);

nums.sort(reverse = True);
print(nums);

print(min(nums));
print(max(nums));
print(sum(nums));

# searching for index of number
print(shoes.index('Jordans'));

# is a value in a list?
print('Jordans' in shoes); # True
print('Lakers' in shoes); # False

# loop through list
for item in shoes:
    print(item);
# getting the index as well
for item in enumerate(shoes):
    print(item);
# or
for index, item in enumerate(shoes):
    print(index, item);
# start at specific index
for index, item in enumerate(shoes, start=1):
    print(index, item);

# list into strings
shoes = ['Nikes', 'Adidas', 'Dock Martens', 'Jordans'];
shoes_str = ' - '.join(shoes);
print(shoes_str);

# original list
new_list = shoes_str.split(' - ')
print(new_list);

# tuples (immutable)
# uses () instead of []
tuple_1 = ('jump', 'walk', 'run');
tuple_2 = tuple_1;

print(tuple_1);
print(tuple_2);

# cannot modify the tuple list

# sets are values that are undordered and have no duplicates
shoes_set = {'Nikes', 'Adidas', 'Dock Martens', 'Jordans'};
print(shoes_set);
