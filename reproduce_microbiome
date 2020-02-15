import pandas as pd
df=pd.read_excel('data.xlsx', sep = "\t", header = 0)
#clean all NaN in phylum and specie
data=df.dropna(subset=["Phylum", "Species"])
data=data.iloc[:,3:]


#get col_sum
data['col_sum'] = df.sum(axis=1)

#sort by col_sum
data.sort_values('col_sum', ascending = False, inplace=True)

#get top 19 col_sum and their species
top_col_species=data['Species'][:21]

#drop other cols
data_new=data.drop(columns=['Class', 'Order','Family','Genus'])


#how many species inside of the phylum
ph=data_new.iloc[:,3]
dic={}
for i in ph:
    if i in dic:
        dic[i]+=1
    else: dic[i]=1
    
    
#make a dictionary that key is phylum, value is specie
spdic={}
for j in range(len(df.iloc[:,8])):
    if df.iloc[:,3][j] in spdic:
        spdic[df.iloc[:,3][j]] += [df.iloc[:,8][j]]
        
    else: spdic[df.iloc[:,3][j]] = [df.iloc[:,8][j]]
    
#find top_phylums that have top species 
ls_top_phy=[]
for spe in top_col_species:
    for key in spdic:
        if spe in spdic[key]:
            if key not in ls_top_phy:
                ls_top_phy += [key]
print(ls_top_phy)


#calculate the sum of others except top species in the phylum

#get data of top 19 sepcies
df_top_species=data.loc[data_new['Species'].isin(top_col_species)]
#print(df_top_species)
#find that some species have same name but in different row
#group same rows
df_top_spe=df_top_species.groupby('Species').sum()
#print(df_top_spe)#data of top 19 sepcies

#remove top species to get the rare species
ls_top_species=[]
for i in top_col_species:
    ls_top_species += [i]
test=list(data_new['Species'])
for j in ls_top_species:
    test.remove(j)

#sum of rare species in each phylum    
rare_data=data_new[data_new['Species'].isin(test)]
rare_data=rare_data.drop(columns=['Species'])
new_rare_data=rare_data.groupby('Phylum').sum()
new_rare_data.reset_index()
#new_rare_data#data of sum(rare species) in each phylum
    
#get sum(rare species) in top 5 phylum
new_rare_data_t=new_rare_data.T
for i in new_rare_data_t:
    if i not in ls_top_phy:
        del new_rare_data_t[i]
new_rare_data_tr=new_rare_data_t.rename(index={'col_sum':'rare_species'})


#calculate the sum of other phylums except top_phylum
df_top_phylum=data_new.loc[data_new['Phylum'].isin(ls_top_phy)]#data of top 5 phylum
#print(df_top_phylum)

#remove top phylum to get the rare phylum
test_phy=list(data_new['Phylum'])
for j in ls_top_phy:
    test_phy.remove(j)
#print(test_phy)

for phy in new_rare_data:
    if phy in ls_top_phy:
        new_rare_data.drop(phy)
new_rare_data.loc['Row_sum'] = new_rare_data.apply(lambda x: x.sum())        
#print(new_rare_data)

#the count of rare phylum in every sample
df_rare_phylum=new_rare_data.iloc[-1,:]#data of rare phylum in each samples


#add rare phylum in each samples to data
df_rare_phy_t=df_rare_phylum
    
df_top_spe_ap=df_top_spe.append(df_rare_phy_t)
df_top_spe_apr=df_top_spe_ap.rename(index={'Row_sum':'rare_phylum'})


data_a=df_top_spe_apr
#data_a

data_b=new_rare_data_tr.T
#data_b

#produce the result dataframe 
result_d=data_a.append(data_b)
result_data=result_d.iloc[:,:-2]


#seperate control and patients 
result_seperate_control=pd.DataFrame(result_data,columns=['ES_001t','ES_007t','ES_010t','ES_014t','ES_017t','ES_019t','ES_024t','ES_043t','ES_046t','ES_048t','ES_080t','ES_108t','ES_116t','ES_132t','ES_137t','ES_147t'])
#result_seperate_control
result_seperate_patient=pd.DataFrame(result_data,columns=['ES_069t','ES_088t','ES_089t','ES_095t','ES_099t','ES_104t','ES_106t','ES_107t','ES_110t','ES_114t','ES_158t','ES_207t','ES_208t','ES_209t','ES_210t','ES_211t'])
#result_seperate_patient


#transfer dataframe to array for clustering
re_control=result_seperate_control.iloc[:-6,:]
re_control=re_control.values

re_patient=result_seperate_patient.iloc[:-6,:]
re_patient=re_patient.values

import numpy as np
np.save('re_control',re_control)
np.save('re_patient',re_patient)


#transfer dataframe to array for clustering
re=result_data.iloc[:-6,:]
re_df=re.values
print(re_df.shape)
import numpy as np
np.save('re_df',re_df)


####### visualization
import matplotlib.pyplot as plt
import numpy as np
import seaborn

#get a clean dictionary that only contain top species 
#print(spdic)
top_spe=[]
for top_sp in top_col_species:
    top_spe += [top_sp]
#print(top_spe)
clean_dic={}
for i in spdic:
    for j in spdic[i]:
        if j in top_spe:
            if i in clean_dic: 
                if j not in clean_dic[i]:
                    clean_dic[i] += [j]
            else: clean_dic[i] = [j]
for i in clean_dic:
    clean_dic[i] += [i] 
    
#manually sorted species by phylum
order_spe=['Atopobium parvulum', 'Rothia mucilaginosa', 'Rothia dentocariosa', 'Actinomyces odontolyticus', 'Actinobacteria','Campylobacter concisus', 'Delftia acidovorans', 'Neisseria flavescens', 'Neisseria subflava', 'Proteobacteria','Streptococcus mitis', 'Veillonella sp. 6_1_27', 'Veillonella sp. 3_1_44', 'Streptococcus gordonii', 'Veillonella parvula', 'Streptococcus pneumoniae', 'Streptococcus salivarius', 'Streptococcus oralis', 'Streptococcus sp. oral taxon 071', 'Firmicutes','Fusobacterium periodonticum', 'Fusobacteria','Prevotella melaninogenica', 'Bacteroidetes','rare_phylum']
df.reindex(index=order_spe)

#how many color should I use
for i in clean_dic:
    print(len(clean_dic[i]))
len(order_spe)

#get the list of color and give it to each species
ls1=seaborn.color_palette("Blues",n_colors=5)
ls2=seaborn.color_palette('YlOrBr',n_colors=5)
ls3=seaborn.color_palette('Purples',n_colors=10)
ls4=seaborn.color_palette('Accent_r',n_colors=2)
ls5=seaborn.color_palette("BuGn_r",n_colors=2)
ls6=seaborn.color_palette('YlGn',n_colors=1)
ls=ls1+ls2+ls3+ls4+ls5+ls6

result_data=result_data.T
df = result_data.div(result_data.sum(axis=1), axis=0)

plot = df.plot.bar(stacked=True,color=ls)

font1 = {'size': 5.2}
legend = plot.legend(prop=font1,loc=2,bbox_to_anchor=(1, 1))
#plot = result_data.plot.bar(stacked=True,color=ls);
plot

#result_seperate_control
result_data_p=result_seperate_patient.T
df_p = result_data_p.div(result_data_p.sum(axis=1), axis=0)
p_p=df_p.plot.bar(stacked=True,color=ls)

font1 = {'size': 5.2}
legend = plt.legend(prop=font1,loc=2,bbox_to_anchor=(1, 1))
p_p

result_data_c=result_seperate_control.T
df_c = result_data_c.div(result_data_c.sum(axis=1), axis=0)

p_c=df_c.plot.bar(stacked=True,color=ls)

font1 = {'size': 5.2}
legend = plt.legend(prop=font1,loc=2,bbox_to_anchor=(1, 1))
p_c



######## further analysis
import numpy as np
import pandas as pd
data=np.load('re_control.npy')
import seaborn


df=pd.read_excel('data.xlsx', sep = "\t", header = 0)
pheno=pd.read_excel('peerj-03-1140-s003.xlsx', sep = "\t", header = 0, index_col = 1)
df = df.drop(df.columns[0:10], axis =1)
pheno["colors"] = ['r' if g == "Yes" else "b" for g in pheno.cigsmoker]
pheno
df.sum(axis=0)

df_log =np.log(df+1)

seaborn.clustermap(df_log,z_score=2,row_cluster=True, col_cluster=True,col_colors=pheno.colors)
