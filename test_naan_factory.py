# Import functions, define and run tests

from naan_factory_functions import *

#1
#As a user, I can use the make_dough with water
#and flour to make dough.

print("calling make_dough with water flour, expect 'dough")
print(make_dough('wheat', 'flour') == 'dough')
print('got: ', (make_dough('wheat', 'flour')))