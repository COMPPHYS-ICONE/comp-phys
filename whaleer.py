import datetime


class Whale:
    def __init__(self, name, sex):
        print 'A {:s} whale named {:s} is born'.format(sex, name)
        self.name = name
        self.sex = sex
        self.age = datetime.timedelta()
    def sing(self):
        print '\a', '\a', '\a', '\a', '\a'
        return 
    def __str__(self):
        return 'A whale named {:s} {:s}'.format(self.name, self.age)
    

w = Whale('Splash', 'M')

print w
#print w.name

print w.age
w.sing()
