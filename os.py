# Interact with the underlying operating system
import os
import datetime
import time
import calendar

path = '/Users/clientepc/Documents/python_practice'
print(path)
# view attributes and method we have access to in this module
print(dir(os))
print(dir(datetime))
print(dir(time))
print(dir(calendar))

# print current working directory
print(os.getcwd())

# if i wanted to change directory
# os.chdir('/Users/clientepc/Documents/')
print(os.getcwd())

#make new files
# os.mkdir('top_level/bottom_level') # will error out because top level isnt available
# os.makedirs('top_level/bottom_level') # works better

# remove files
# os.removedir('top_level/bottom_level')

print(os.listdir(path))

# rename files
# os.rename('original_filename', 'new_filename.txt')

# file stats
print(os.stat('new_filename.txt'))
# time stamp
print(os.stat('new_filename.txt').st_mtime)
# modify
real_time = os.stat('new_filename.txt').st_mtime
print(datetime(real_time))
