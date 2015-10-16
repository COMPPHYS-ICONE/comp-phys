'''

simulates a dolphin population for a certain number of years

saves a graph of evolving population

poor attempt at a genealogy tree

have mercy on my soul

uncomment find_names() if you want to create the text file of names

'''


import numpy as np
import random as rnd
import urllib2 
import re
import networkx as nx
import matplotlib.pyplot as plt



#################################################################################

    
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
    def prob_eligible(self):
        if (self.age > 8 and self.since_laid > 5):
            return True
    def eligibility(self, partner):
        if (self.sex != partner.sex\
        and self.mother != partner.name\
        and self.father != partner.name\
        and partner.mother != self.name\
        and partner.father != self.name\
        and self.age >= 8 and self.since_laid > 5\
        and partner.age >= 8 and partner.since_laid > 5\
        and abs(self.age-partner.age) <= 10\
        and (self.mother != partner.mother or self.father != partner.father)):
            return True
        
        

#advances the year and prints all the appropriate statements   
def advance_year(i):
    global year
    global breeding 
    if (i == 0 or i == 25 or i == 50 or i == 75 or i ==100 or i ==125):
        print '**********************'
        print 'entering year {:g} with {:g} dolphins, with {:g} breeding.'\
        .format(year,len(living_dolphins),breeding)
    breeding = 0
    
    for k in living_dolphins:
        k.aging()
        if k.prob_eligible() == True and k.sex == 'Male':
            for j in living_dolphins:
                marvin_gaye(k,j)
        if (k.age > k.death and k.dead == 0):
            dead_dolphins.append(k)
            k.dead = 1
        if k.dead ==1:
            del k
    if i == 100:
        print 'At year 100, there are {:g} living dolphins. There have been {:g} births, in total.'\
        .format(len(living_dolphins), (len(living_dolphins)+len(dead_dolphins)))
    if i == 149:
        print '**********************'
        print 'at year 149, there are {:g} living dolphins'.format(len(living_dolphins))
    
    year += 1
    
    
        
        
#sexytime and babytime        
def marvin_gaye(self,partner):
    if self.eligibility(partner) == True:
        self.got_laid()
        partner.got_laid()
        global breeding
        breeding +=1
        if self.sex == 'Male':
            temp = gender()
            if temp == 'Male':
                living_dolphins.append(Dolphins(make_name(temp).next(),partner.name, self.name, temp))
            if temp == 'Female':
                living_dolphins.append(Dolphins(make_name(temp).next(),partner.name, self.name, temp))
        if self.sex == 'Female':
            temp = gender()
            if temp == 'Male':
                living_dolphins.append(Dolphins(make_name(temp).next(),self.name, partner.name, temp))
            if temp == 'Female':
                living_dolphins.append(Dolphins(make_name(temp).next(),self.name, partner.name, temp))
        

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
            for i in range(0, len(guy_names_list)):
                yield guy_names_list[i]
                i +=1
        except StopIteration:
            for i in range(0, len(guy_names_list)):
                yield middle_names_list[i]
                i +=1
         
    if sex == 'Female':
        try:
            for i in range(0, len(girl_names_list)):
                yield girl_names_list[i]
                i +=1
        except StopIteration:
            for i in range(0, len(guy_names_list)):
                yield middle_names_list[i]
                i +=1

                


    
                
                
#find_names() #uncomment to create name files

#instansiating lists and dictionaries
mean = {}
std = {}
living_dolphins = []
dead_dolphins = []
dolphins_num = []
global dolphins_year
dolphins_year = []
dolphins_mean = []
dolphins_std = []
full_dict = {}
guys_names = make_name('Male')
girls_names = make_name('Female')
year = 0
breeding = 0        
for i in ['Ted', 'Bobby']:
    living_dolphins.append(Dolphins(i,0,1,'Male'))
for i in ['Terry', 'Alisha']:
    living_dolphins.append(Dolphins(i,2,3,'Female'))
                
#######################################################
        
        
filename = "/Users/labuser/comp-phys/guys_names.txt" 
with open(filename,"r") as f:
    x = f.read()
    guy_names_list = eval(x)
    rnd.shuffle(guy_names_list)
    
            
filename = "/Users/labuser/comp-phys/gals_names.txt"
with open(filename,"r") as f:
    x = f.read()
    girl_names_list = eval(x)
    rnd.shuffle(girl_names_list)
    
filename = "/Users/labuser/comp-phys/middle_names.txt"
with open(filename,"r") as f:
    x = f.read()
    middle_names_list = eval(x)
    rnd.shuffle(middle_names_list)                


    
                
#Encompassing trial functions
        


def run_trial(j):
    print ''
    print 'Trial No. {:g}'.format(j)
    for i in range(0,150):
        advance_year(i)
        dolphins_year.append(len(living_dolphins))
        if i == 70:
            my_dolphin = living_dolphins[1] # My main character
    
            
def run_all_trials(n):
    for k in range (1,n+1):
        run_trial(k)
        global year
        year = 0
        global breeding
        breeding = 0
        global living_dolphins
        living_dolphins = [Dolphins('Billy',0,1,'Male'), Dolphins('Joey',2,3,'Male'), \
                           Dolphins('Terry',4,5,'Female'), Dolphins('Patricia',6,7,'Female')]
        dolphins_num.append(dolphins_year)
        global dolphins_year
        dolphins_year = []
        global dead_dolphins
        dead_dolphins = []
    for j in range(0,150):
        dolphins_mean.append(np.mean([i[j] for i in dolphins_num]))
        dolphins_std.append(np.std([i[j] for i in dolphins_num]))
    
    return np.array(dolphins_mean), np.array(dolphins_std)       
            

    
    
meanizzle, stdizzle = run_all_trials(10) #runs the trials and saves mean and std


#Graphing components below

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

G.add_edge('Main Character','Dad',weight=0.8)
G.add_edge('Main Character','Mom',weight=0.8)
G.add_edge('Sister','Mom',weight=0.8)
G.add_edge('Sister','Dad',weight=0.8)
G.add_edge('Half-Brother','Mom',weight=1.6)
G.add_edge('Half-Sister','Dad',weight=1.6)

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
