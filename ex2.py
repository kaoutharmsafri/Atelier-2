def split_list(l):
    lengh=len(l)//3
    a=l[:lengh]
    b=l[lengh:lengh*2]
    c=l[lengh*2:]
    return a,b,c
def inverse(l):
    newl=[]
    i=len(l)-1
    while(i>=0):
        newl.append(l[i])
        i-=1
    return newl
l=[11, 45, 8, 23, 14, 12, 78, 45, 89]
l1,l2,l3=split_list(l)
print(inverse(l1),end="")
print(inverse(l2),end="")
print(inverse(l3))