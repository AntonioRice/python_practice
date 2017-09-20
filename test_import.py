# importing entire module
# or
# from my_module imoport * <- but we cannot tell what came from this module
import my_module

teams = ['Lakers', 'GSW', 'Wolves', 'Heat']

index = my_module.find_index(teams, 'Wolves')
print(index)

# we could also import module as mm
# import my_module as mm
# import function in module: 'from mu_module import find_index'
# python looks for modules using "sys"
# path, standard library directives, site packages directories from 3rd party

import sys
print(sys.path)

# if module is not found, you are able to append the directory into sys.path
# or change python environment variable

# STANDARD LIBRARY examples
import random

random_teams = random.choice(teams)
print(random_teams)

import math
import datetime
import calendar

# returning leap year using standard library: calendar
print(calendar.isleap(2019))
# returning today's date
today = datetime.date.today()
print(today)

# viewing entire standard library
import os

print(os.__file__)
