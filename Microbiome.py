############### overview the data
new=[]
bodysites=[]
dic={}
with open('./Desktop/550_hw/v13_map_uniquebyPSN.txt','r') as f:
    for l in f.readlines():
        linestrlist = l.split("\t")
        #print(linestrlist)#become list
        if linestrlist[2] == '1':
            new += [linestrlist]#only select the visitno1 elements
for i in new:
    bodysites += [i[5]]
    #print(i[5])
#print(bodysites)
            
for i in bodysites:
    if i in dic:
        dic[i] += 1
    else: dic[i] =1
#print(dic)   
import matplotlib.pyplot as plt    
import numpy as np
#print(body)
#plt.plot(dic)
dic_x=[i for i in dic]
dic_y=[dic[i] for i in dic]

bar_1=plt.bar(dic_x,dic_y)
import pylab as pl
pl.xticks(rotation=90)


################# female or male in body site
new=[]
bodysites=[]
female={}
male={}
dic={}
site=[]
with open('./Desktop/550_hw/v13_map_uniquebyPSN.txt','r') as f:
    for l in f.readlines():
        linestrlist = l.split("\t")
        if linestrlist[2] == '1':
            new += [linestrlist]#only select the visitno1 elements
for i in new:
    bodysites += [[i[5],i[3]]]
#print(bodysites)
for i in bodysites:
    if i[0] not in site:
        site += [i[0]]
#print(site)
for i in bodysites:
    if i[1] == 'female':
        if i[0] in female:
            female[i[0]] += 1
        else: female[i[0]] =1
    else:
        if i[0] in male:
            male[i[0]] += 1
        else: male[i[0]] =1
for i in bodysites:
    if i[0] not in site:
        site += [i[0]]
        
for i in site:
    if i not in male:
        male[i]=0
    if i not in female:
        female[i]=0
        
#print(site)
        
dic_fx=[i for i in female]
dic_fy=[female[i] for i in female]
dic_mx=[i for i in female]
dic_my=[male[i] for i in female]

#print('female:',dic_fy)
#print('male:',dic_my)
#print('female:',dic_fx)
#print('male:',dic_mx)
import matplotlib.pyplot as plt    
import numpy as np

N = len(female)
ind = np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars

fig = plt.figure()
ax = fig.add_subplot(111)
rects1 = ax.bar(ind, dic_fy, width)
rects2 = ax.bar(ind+width, dic_my, width)


ax.set_ylabel('number')
ax.set_title('female/male in bodysites')
ax.set_xticks(ind + width / 2)
ax.set_xticklabels( (i for i in female) )
ax.legend( (rects1[0], rects2[0]), ('female', 'male') )
import pylab as pl
pl.xticks(rotation=90)
plt.show()

########################## write down the result
n=1
name=[i for i in site]
save=[]
something=''
#print(name)
for i in new:
    save += [[i[0],i[5]]]
for i in name:
    n_str=str(n)
    filename=n_str+i+'.txt'
    f=open( filename,'w')
    for j in save:
        if i == j[1]:
            something += j[0]+'///'
    


    f.write(something)
    f.close()
    n += 1
