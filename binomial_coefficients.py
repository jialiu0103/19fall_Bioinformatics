class binomial_coefficients:
    def __init__(self):
        self.dic={}
        
    def get_n(self,n): 
        a=0
        b=1
        ls=[]
        t=1
        if n not in self.dic:
            if n==0: 
                return [1] 
                self.dic[1] = [1]
            elif n==1: 
                return [1,1]
                self.dic[2]=[1,1]
            else:
                while len(ls) < n-1:
                    t += 1
                    bs=binomial_coefficients.get_n(n - 1)
                    self.dic[t]=bs
                    ls = ls + [bs[a] + bs[b]]
                    a += 1
                    b += 1
                result=[1]+ls+[1]
                self.dic[n]=result    
            
            return result
        else: return self.dic[n]
        
    def get_nk(self, n, k):
        get_ls=binomial_coefficients.get_n(n)
        return get_ls[k]
    
    def save_pt(self, n, file_name = 'pascal_triangle.txt'):
        f = open("pascal_triangle.txt", 'w+')
        for i in range(n):
            h=binomial_coefficients.get_n(i)
            line= str(h).replace('[', '').replace(']', '').replace(',', '')
            print('{:^60}'.format(line),file=f)


###### call the class
binomial_coefficients=binomial_coefficients()
binomial_coefficients.get_n(5)
binomial_coefficients.get_nk(10, 8)
###### save the file
binomial_coefficients.save_pt(10, file_name = 'pascal_triangle.txt')
