l1=[47, 64, 69, 37, 76, 83, 95, 97]
my_dict={'Yassine':47, 'Imane':69, 'Mohammed':76, 'Abir':97}
for i in l1:
    for j in my_dict.values():
        if i == j:
            break
        else:
            l1.remove(i)
            break
print("la liste après modification:",l1)