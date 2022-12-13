List=[11, 45, 8, 11, 23, 45, 23, 45, 89]
c=[]
my_dict = {} 
for i in range (len(List)-1):
    k=0
    for j in range (len(List)-1):
        if List[i]==List[j]: 
            k+=1  
    c.insert(i,k)
for i in range (len(List)-1):
    my_dict.setdefault(List[i],c[i])
my_dict.setdefault(List[-1],c[-1])
print(my_dict)
