import numpy as np
import random as rnd
import urllib2 
import re


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
        self.since_laid = 0
        self.dead = 0
    def aging(self):
        self.age +=1
        self.since_laid +=1
    def got_laid(self):
        self.since_laid = 0
    def eligibility(self, partner):
        if (self.sex != partner.sex \
        and self.age >= 8 and self.since_laid >= 5\
        and partner.age >=8 and partner.since_laid >= 5\
        and abs(self.age-partner.age) < 10\
        and (self.mother != partner.mother or self.father != partner.father)):
            return True
        
        
living_dolphins = []
dead_dolphins = []
guys_names = make_name('Male')
girls_names = make_name('Female')
year = 0
breeding = 0        
for i in ['Ted', 'Bobby']:
    living_dolphins.append(Dolphins(i,0,1,'Male'))
for i in ['Terry', 'Alisha']:
    living_dolphins.append(Dolphins(i,2,3,'Female'))
    
    
def advance_year():
    global year
    global breeding
    print 'entering year', year, 'with', len(living_dolphins),'dolphins, with',breeding,'breeding.' 
    breeding = 0
    year += 1
    for i in living_dolphins:
        i.aging()
        for j in living_dolphins:
            marvin_gaye(i,j)
    
        
        
        
def marvin_gaye(self,partner):
    if self.eligibility(partner) == True:
        self.got_laid()
        partner.got_laid()
        global breeding
        breeding +=1
        if self.sex == 'Male':
            temp = gender()
            if temp == 'Male':
                living_dolphins.append(Dolphins(guys_names.next(),partner.name, self.name, temp))
                print living_dolphins[-1].name, 'was born!'
            if temp == 'Female':
                living_dolphins.append(Dolphins(girls_names.next(),partner.name, self.name, temp))
                print living_dolphins[-1].name, 'was born!'
        if self.sex == 'Female':
            temp = gender()
            if temp == 'Male':
                living_dolphins.append(Dolphins(guys_names.next(),self.name, partner.name, temp))
                print living_dolphins[-1].name, 'was born!'
            if temp == 'Female':
                living_dolphins.append(Dolphins(girls_names.next(),self.name, partner.name, temp))
                print living_dolphins[-1].name, 'was born!'
        

        
def find_names():
    boy_names = ''
    girl_names = ''
    for i in range(1,226):
        url = 'http://www.prokerala.com/kids/baby-names/boy/page-{:g}.html'.format(i)
        infile = urllib2.urlopen(url) 
        boy_names += infile.read()   
        infile.close()  
    for i in range(1,171):
        url = 'http://www.prokerala.com/kids/baby-names/girl/page-{:g}.html'.format(i)
        infile = urllib2.urlopen(url)
        girl_names += infile.read()
        infile.close()
    guys_names1 = re.findall('(.*nameDetails">)(.*)(</)', boy_names)
    guys_names = []
    gals_names1 = re.findall('(.*nameDetails">)(.*)(</)', girl_names)
    gals_names = []
    for txt in guys_names1:
        text = txt[1]
        text2 = text.strip('</span>')
        guys_names.append(text2)
    for txt in gals_names1:
        text = txt[1]
        text2 = text.strip('</span>')
        gals_names.append(text2)
    dir_path = "/Users/labuser/comp-phys/"
    filenm1 = dir_path + "guys_names.txt"                
    with open(filenm1,"w") as f:
        f.write(str(guys_names)) 
    filenm2 = dir_path + "gals_names.txt"                
    with open(filenm2,"w") as f:
        f.write(str(gals_names)) 
    
#find_names()    
    
def make_name(sex):
    if sex == 'Male':
        filename = "/Users/labuser/comp-phys/guys_names.txt" 
        with open(filename,"r") as f:
            x = f.read()
            names_list = eval(x)
            rnd.shuffle(names_list)
            for i in range(0, len(names_list)):
                yield names_list[i]
                i +=1
         
    if sex == 'Female':
        filename = "/Users/labuser/comp-phys/gals_names.txt"
        with open(filename,"r") as f:
            x = f.read()
            names_list = eval(x)
            rnd.shuffle(names_list)
            for i in range(0, len(names_list)):
                yield names_list[i]
                i +=1
                

        
        


for i in range(0,40):
    advance_year()
    for j in living_dolphins:
        if (j.age > j.death and j.dead == 0):
            dead_dolphins.append(j)
            print j.name,'has died!'
            j.dead = 1
        else:
            print j.name,'is',j.age,'years old'
    for j in living_dolphins:
        if j.dead ==1:
            del j
            
#print len(living_dolphins)
#print len(dead_dolphins)