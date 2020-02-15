import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sps
np.set_printoptions(precision=3)

N=4900#number of samples
n=1000#number of genes

# function that generates a gene expression
def gene_expression(mu, std, N):
    
    return np.random.normal(loc=mu, scale=std, size=N)
    
class trial():
    """Simulates veterinary trial."""
    def __init__(self, all_genes=10**3):
        self.all_genes=all_genes
    def run_trial(self):
        self.normal_cells = gene_expression(0, 1, self.all_genes)
        cancer_one=gene_expression(1,1,10)
        cancer_two=gene_expression(0.1,1,100)
        cancer_rest=gene_expression(0,1,890)
        first_two=np.append(cancer_one,cancer_two)
        self.cancer_cells= np.append(first_two,cancer_rest)
        gene_to_index = {ind:name for ind, name in enumerate(self.cancer_cells)}
        
        return {'normal_cells':self.normal_cells, 'cancer_cells':self.cancer_cells, 'gene_to_index':gene_to_index}
        
normal_set=np.zeros((n,N))
cancer_set=np.zeros((n,N))
for i in range(N):
    my_trial = trial()
    outcome = my_trial.run_trial()
    normal_set[:,i]=outcome['normal_cells']
    cancer_set[:,i]=outcome['cancer_cells']
print(normal_set.shape,cancer_set.shape)

# need to sample two random subdivisions multiple times
class random_groupings:
    def __init__(self, group_one, group_two):
        self.n_one = group_one.shape[1] # number of samples in group one
        self.n_two = group_two.shape[1] # same for group two
        self.n_all = self.n_one + self.n_two # size of the data
        self.all = np.concatenate((group_one, group_two), axis=1) # merged data
    def generate_random_split(self):
        ind = np.arange(self.n_all)
        np.random.shuffle(ind)
        temp = self.all.copy() # copy to avoid corruption by user
        temp = temp[:, ind] # now the columns are shuffled
        go = temp[:, :self.n_one] # group one
        gt = temp[:, self.n_one:] # group two
        return (go, gt)
        
# rear r from the data
m_normal = normal_set.mean(axis=1)
m_cancer = cancer_set.mean(axis=1)

class significance_test:
    def __init__(self, simulation_number=10**3):
        self.simulation_number = simulation_number
        # properties of actual data
        self.n_c = m_normal
        self.c_c = m_cancer
        self.R = np.zeros((self.simulation_number,1000)) # store values 
        
    def permutation(self):
        rg = random_groupings(normal_set, cancer_set)
        for i in range(self.simulation_number):
            go, gt = rg.generate_random_split()
            self.R[:,i] = np.abs(gt.mean(axis=1)-go.mean(axis=1)) 
        
    def perform_test(self):
        p_value = np.zeros((1000))
        for i in range(self.simulation_number):
            p_value[i] = np.sum(self.R[i,:]>np.abs(self.n_c[i]-self.c_c[i]))/1000   #get p_values for each gene
        p_ind = np.argsort(p_value)                          #sort
        p_value_sorted = p_value[p_ind]
        q_value = np.zeros((len(p_value)))
        for j in range(len(p_value)):
            q_value[j] = p_value_sorted[j]*1000/(j+1)   #get q_value
        return q_value,p_ind,p_value_sorted
        
my_trial = trial()  
my_trial.run_trial()
st = significance_test()
st.permutation()              
q_value,ind,p_value = st.perform_test() 
alpha=0.05
print(q_value)
num_significant = np.sum(q_value<=alpha)                      
cancer_o = 0
cancer_t = 0
for mi in ind[:num_significant]:
    if mi < 10:
        cancer_o += 1                                       
    elif mi in range(10,110):                                  
        cancer_t += 1                                       
print(cancer_o,cancer_t)
print(q_value[q_value<=alpha])

#By change N in the second cell(100,200,500,1000,5000...), I get the results.
#when sample size is near 200, I can get all 10 genes whose mean=1.
#when sample size is near 5000, I can get all 10 genes whose mean=1 and all 100 genes whose mean=0.1.
#If I want to get the accurate result, I should run the script more than one time and get the mean of it, but it takes too much time to run the script. So I just did one time.
