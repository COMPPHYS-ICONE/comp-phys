'''

run_all_trials simulates a dolphin population for a certain number of years
& saves a graph of evolving population + graph of geneology(sort of) for random 
dolphin picked at year 70
 
how_many_males calculates the minimum probability of males needed to sustain
the population for 150 years


'''


import numpy as np
import random as rnd
import urllib2 
import re
import networkx as nx
import matplotlib.pyplot as plt
import copy



#################################################################################
global year
year = 0
global breeding
breeding = 0
global living_dolphins
global dolphins_year
global my_dolphin
global dead_dolphins
global p
global alpha

p = .5
half =.5


#instansiating lists and dictionaries
mean = {}
std = {}
living_dolphins = []
dead_dolphins = []
dolphins_num = []
dolphins_year = []
dolphins_mean = []
dolphins_std = []
full_dict = {}
p_list = []

      




def gender(p):
    if np.random.rand() > p:
        return 'Female'
    else:
        return 'Male'


class Dolphins:
    def __init__(self, name, mother, father, sex = gender(p)):
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
    def prob_eligible(self):
        if (self.age > 8 and self.since_laid > 5):
            return True
    def eligibility(self, partner):
        if (self.sex != partner.sex\
        and self.mother != partner.name\
        and self.father != partner.name\
        and partner.mother != self.name\
        and partner.father != self.name\
        and self.age > 8 and self.since_laid > 5\
        and partner.age > 8 and partner.since_laid > 5\
        and abs(self.age-partner.age) < 10\
        and (self.mother != partner.mother or self.father != partner.father)):
            return True
        
        
living_dolphins = [Dolphins('Billy','Mom','Dad','Male'), Dolphins('Joey','Mom',"Dad",'Male'), \
                           Dolphins('Terry','Mommy','Daddy','Female'), Dolphins('Patricia','Mommy','Daddy','Female')]


#advances the year and prints all the appropriate statements   
def advance_year(i,p):
    global year
    global breeding
    if (i == 0 or i == 25 or i == 50 or i == 75 or i ==100 or i ==125):
        print '**********************'
        print 'entering year {:g} with {:g} dolphins, with {:g} breeding.'\
        .format(year,len(living_dolphins),breeding)
    breeding = 0
    for k in living_dolphins:
        k.aging()
        if (k.age > k.death and k.dead == 0):
            dead_dolphins.append(k)
            k.dead = 1
        if k.dead ==1:
            living_dolphins.remove(k)
            del k
        elif k.prob_eligible() == True and k.sex == 'Male':
            for j in living_dolphins:
                marvin_gaye(k,j,p)
    if i == 100:
        print 'At year 100, there are {:g} living dolphins. There have been {:g} births, in total.'\
        .format(len(living_dolphins), (len(living_dolphins)+len(dead_dolphins)))
    if i == 149:
        print '**********************'
        print 'at year 149, there are {:g} living dolphins'.format(len(living_dolphins))
    
    year += 1
    return living_dolphins
    
    
        
        
#sexytime and babytime        
def marvin_gaye(self,partner,p):
    global breeding
    if self.eligibility(partner) == True:
        self.got_laid()
        partner.got_laid()
        breeding +=1
        temp = gender(p)
        if self.sex == 'Male':
            if temp == 'Male':
                living_dolphins.append(Dolphins(jesus.next(),partner.name, self.name, temp))
            if temp == 'Female':
                living_dolphins.append(Dolphins(jesus.next(),partner.name, self.name, temp))
        if self.sex == 'Female':
            if temp == 'Male':
                living_dolphins.append(Dolphins(jesus.next(),self.name, partner.name, temp))
            if temp == 'Female':
                living_dolphins.append(Dolphins(jesus.next(),self.name, partner.name, temp))
        

#draws names from internet        
def find_names():
    boy_names = ''
    girl_names = ''
    middle_names = ''
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
    middle_names1 = re.findall('(.*nameDetails">)(.*)(</)', middle_names)
    middle_names = []
    for txt in guys_names1:
        text = txt[1]
        text2 = text.strip('</span>')
        guys_names.append(text2)
    for txt in gals_names1:
        text = txt[1]
        text2 = text.strip('</span>')
        gals_names.append(text2)
    for txt in middle_names1:
        text = txt[1]
        text2 = text.strip('</span>')
        middle_names.append(text2)
    dir_path = "/Users/labuser/comp-phys/"
    filenm1 = dir_path + "guys_names.txt"                
    with open(filenm1,"w") as f:
        f.write(str(guys_names)) 
    filenm2 = dir_path + "gals_names.txt"                
    with open(filenm2,"w") as f:
        f.write(str(gals_names))
    filenm3 = dir_path + "middle_names.txt"                
    with open(filenm3,"w") as f:
        f.write(str(middle_names))


#assigns names to dolphins    
def make_name(sex):
    
    if sex == 'Male':
        try:
            for i in range(0, 5*len(guy_names_list)):
                yield guy_names_list[i]
        except StopIteration:
            for i in range(0, 5*len(guy_names_list)):
                yield middle_names_list[i]
         
    if sex == 'Female':
        try:
            for i in range(0, 5*len(girl_names_list)):
                yield girl_names_list[i]
        except StopIteration:
            for i in range(0, 5*len(guy_names_list)):
                yield middle_names_list[i]

                
jesus = make_name('Male')
jesusess = make_name('Female')              
                
#find_names() #uncomment to create name files


                
#######################################################
        
        
filename = "/Users/labuser/comp-phys/guys_names.txt" 
with open(filename,"r") as f:
    x = f.read()
    guy_names_list = eval(x)
    guy_names_list += guy_names_list
    guy_names_list += guy_names_list
    guy_names_list += guy_names_list
    rnd.shuffle(guy_names_list)
    
            
filename = "/Users/labuser/comp-phys/gals_names.txt"
with open(filename,"r") as f:
    x = f.read()
    girl_names_list = eval(x)
    girl_names_list += girl_names_list
    girl_names_list += girl_names_list
    girl_names_list += girl_names_list
    rnd.shuffle(girl_names_list)
    
filename = "/Users/labuser/comp-phys/middle_names.txt"
with open(filename,"r") as f:
    x = f.read()
    middle_names_list = eval(x)
    middle_names_list += middle_names_list
    middle_names_list += middle_names_list
    middle_names_list += middle_names_list
    rnd.shuffle(middle_names_list)                


    
                
#Encompassing trial functions
        


def run_trial(j,p):
    global living_dolphins
    global dolphins_year
    print ''
    print 'Trial No. {:g}'.format(j)
    for i in range(0,150):
        advance_year(i,p)
        dolphins_year.append(len(living_dolphins))
        if i == 120:
            rnd.shuffle(living_dolphins)
            global my_dolphin
            global my_dolphins_list
            try:
                my_dolphin = living_dolphins[1]
                my_dolphins_list = living_dolphins# My main character
            except IndexError:
                print 'All the dolphins have died out! Please try again!'

#specific to part b
def run_trial_male(j,p):
    global living_dolphins
    global dolphins_year
    print ''
    for i in range(0,150):
        advance_year(i,p)
        if len(living_dolphins) <= 1:
            print 'The dolphin population has died out!'
            return 0
        if i == 149:
            if len(living_dolphins) >= 1:
                print 'The dolphin population has survived! The probability of males was {:g}'.format(p)
                return 1
    
            
def run_all_trials(n,p = half):
    global year
    global breeding
    global dolphins_year
    global living_dolphins
    global dead_dolphins
    global alpha
    alpha = 1
    for k in range (1,n+1):
        if k == n+1:
            run_trial(k,p)
        else:
            run_trial(k,p)
            year = 0
            breeding = 0
            living_dolphins = [Dolphins('Billy','Mom','Dad','Male'), Dolphins('Joey','Mom',"Dad",'Male'), \
                               Dolphins('Terry','Mommy','Daddy','Female'), Dolphins('Patricia','Mommy','Daddy','Female')]
            dolphins_num.append(dolphins_year)
            dolphins_year = []
            dead_dolphins = []
    for j in range(0,150):
        dolphins_mean.append(np.mean([i[j] for i in dolphins_num]))
        dolphins_std.append(np.std([i[j] for i in dolphins_num]))
    
    return np.array(dolphins_mean), np.array(dolphins_std)       
            
#specific to part b    
def how_many_males(n):
    global year
    global breeding
    global dolphins_year
    global living_dolphins
    global dead_dolphins
    global p
    global alpha
    alpha = 0
    for k in range (1,n+2):
        p_list.append(p)
        p = 0
        myvar = 0
        while myvar != 1:
            myvar = run_trial_male(k,p)
            p+=0.01
            year = 0
            breeding = 0
            living_dolphins = [Dolphins('Billy','Mom','Dad','Male'), Dolphins('Joey','Mom',"Dad",'Male'), \
                               Dolphins('Terry','Mommy','Daddy','Female'), Dolphins('Patricia','Mommy','Daddy','Female')]
            dolphins_num.append(dolphins_year)
            dolphins_year = []
            dead_dolphins = []
    del p_list[0]
    #print p_list
    return np.mean(p_list)

    

#meanizzle, stdizzle = run_all_trials(10) #runs the trials and saves mean and std

#find out the minimum probability of males needed
meanyp = how_many_males(10)
print "\n\n\nThe average minimum probability for males was {:g}".format(meanyp)




#Graphing components below
if alpha == 1: #if running trails for part a not part b
    fig = plt.figure()
    x = np.arange(0.0, len(meanizzle), 1)
    ax = fig.add_subplot(111)
    plt.plot(meanizzle,'r-', lw = 2)
    plt.fill_between(x,meanizzle+stdizzle, meanizzle-stdizzle)
    plt.title('Average Population and Standard Deviation from 10 Trials')
    plt.xlabel('Years')
    plt.ylabel('Number of Living Dolphins')
    plt.savefig("population_growth.pdf")
    plt.show()    






    #genealogy tree general
    G=nx.Graph()

    G.add_edge(my_dolphin.name,my_dolphin.mother,weight=0.8)
    G.add_edge(my_dolphin.name,my_dolphin.father,weight=0.8)
    for names in my_dolphins_list:
        if (names.mother == my_dolphin.mother and names.father == my_dolphin.father):
            G.add_edge(names.name,my_dolphin.mother,weight=0.3)
            G.add_edge(names.name,my_dolphin.father,weight=0.3)
        if (names.mother == my_dolphin.mother and names.father == my_dolphin.father):
            G.add_edge(names.name,my_dolphin.mother,weight=0.3)
            G.add_edge(names.name,my_dolphin.father,weight=0.3) 
        if names.mother == my_dolphin.mother:
            G.add_edge(names.name,my_dolphin.mother,weight=0.5)
        if names.father == my_dolphin.father:
            G.add_edge(names.name,my_dolphin.father,weight=0.5)

    elarge=[(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] >0.5]
    esmall=[(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] <=0.5]

    pos=nx.spring_layout(G)

    nx.draw_networkx_nodes(G,pos,node_size=700)


    nx.draw_networkx_edges(G,pos,edgelist=elarge,
                        width=6)
    nx.draw_networkx_edges(G,pos,edgelist=esmall,
                        width=6,alpha=0.5,edge_color='b',style='dashed')

    nx.draw_networkx_labels(G,pos,font_size=20,font_family='sans-serif')

    plt.axis('off')
    plt.savefig("genealogy.pdf") 
    plt.show() 

