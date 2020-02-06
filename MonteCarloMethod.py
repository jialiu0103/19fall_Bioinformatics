import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
%matplotlib inline
###### start to work
class area():
    def __init__(self,L=12):
        self.L=L
    def draw(self,N=10**6):
        self.trial_x=self.L*(np.random.random(N)-0.5)
        self.trial_y=self.L*(np.random.random(N)-0.5)
    def check(self):
        self.a=((self.trial_x+3)**2+self.trial_y**2)**0.5
        self.b=(self.trial_x**2+self.trial_y**2)**0.5
        self.c=((self.trial_x-3)**2+self.trial_y**2)**0.5
        self.accept= (self.a+self.b+self.c) <= 17
    def calculate(self):
        self.area=(self.accept.sum()*self.L**2)/self.accept.size
        return self.area
    def plot(self):
        f = plt.figure(figsize=(5,5))
        ax = f.add_subplot(111)
        box = mpl.patches.Rectangle((-self.L/2, -self.L/2), self.L, self.L, fill=False, transform=ax.transData, linestyle='-', color='blue')
        ax.add_patch(box)
        area = plt.scatter(self.trial_x,self.trial_y)
        ax.plot(self.trial_x[self.accept], self.trial_y[self.accept], 'r.', markersize=5)
        ax.plot(self.trial_x[~self.accept], self.trial_y[~self.accept], 'b.', markersize=5)
    def phist(self):
        ls=np.zeros(100)
        for i in range(100):
            area.draw()
            area.check()
            ls_result=area.calculate()
            ls[i] = ls_result
        ls_min=min(ls)
        ls_new=ls-ls_min
        #print(ls)
        #print(ls_min)
        #print(ls_new)
        plt.hist(ls)
    
##### run the class
area = area() 
area.draw()
area.check()
print('area:', area.calculate())

####caculate the accuracy
p=area.calculate()/12**2
n=10**6
accuracy = np.sqrt(p*(1-p))/np.sqrt(n)
print(p)
print(accuracy)
#As accuracy << 1%, I achieved this accuracy.

#### plot
area = area() 
area.draw()
area.check()
area.phist()
#they are within 1% of each other
area.plot()
