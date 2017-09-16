nums = [1,2,3,4,5]

# looping through the list
for num in nums:
    print(num)

# breaking when finding specific value
for num in nums:
    if num == 3:
        print('Rabb')
        break
    print(num)
# continue after value found
for num in nums:
    if num == 3:
        print('Rabb')
        continue
    print(num)

# inner loop, each number gets each letter
for num in nums:
    for i in 'abc':
        print(num, i)

# range, will print x many items starting at 0
for i in range(10):
    print(i)

# starting at 1, to 10
for i in range(1, 11):
    print(i)


# while loop

x = 0
while x < 10:
    print('this is', x)
    x += 1
