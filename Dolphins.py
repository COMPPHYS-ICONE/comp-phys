import numpy as np
import random as rnd


def gender():
    if rnd.randint(0,2) == 0:
        return 'Male'
    else:
        return 'Female'


class Dolphins:
    def __init__(self, name, mother, father, sex = gender()):
        self.name = name
        self.sex = sex
        self.age = 0
        self.mother = mother
        self.father = father
        self.death = rnd.gauss(mu = 35, sigma = 5)
        self.active = 0
        self.since_laid = 0
        self.dead = 0
    def aging(self):
        self.age +=1
        self.since_laid +=1
    def got_laid(self):
        self.since_laid = 0
    def eligibiliy(self, partner):
        if (self.sex != partner.sex \
        and self.age >= 8 and self.active == 0\
        and partner.age >=8 and partner.active == 0\
        and abs(self.age-partner.age) < 10\
        and (self.mother != partner.mother or self.father != partner.father)):
            return True