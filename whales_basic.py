'''

Creates a class whale with name, sex, and age. Creates whales from a list of names, randomly assigning genders. See commented out calls at bottom of page for sing and age

'''

import datetime
import time
import random


def sex():
    if random.randrange(2) == 0:
        return 'Male'
    else:
        return 'Female'
    
    


class Whale:
    def __init__(self, name, sex):
        print 'A {:s} whale named {:s} is born'.format(sex, name)
        self.born = datetime.datetime.now()
        self.name = name
        self.sex = sex
        
    def sing(self):
        return '\a \a \a \a \a'
    
    def whale_age(self):
        return datetime.datetime.now() - self.born
    
    def __str__(self):
        return 'A whale named {:s} {:s}'.format(self.name, self.age)
    

whale_names = ['Homer', 'Bart', 'Lisa', 'Marge', 'Maggie', "Santa's Little Helper",\
               'Snowball', 'Otto', 'Moe', 'Ned Flanders', 'Maud Flanders', 'Barney', 'Krusty', 'Sideshow Bob',\
              'Groundskeeper Willie', 'Principal Skinner', 'Chief Wiggum', 'Ralph', 'Montgomerey Burns',\
              'Waylon Smithers']


whale = []
    

    
for i in whale_names:
    whale.append(Whale(i,sex()))

#print whale[0]
print whale[0].whale_age()
print whale[0].sing()
