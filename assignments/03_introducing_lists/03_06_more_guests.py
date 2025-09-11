names = ['Marcello', 'Seyeon', 'Marie']
print(names[0]+', you are invited to the dinner!')
print(names[1]+', you are invited to the dinner!')
print(names[2]+', you are invited to the dinner!')

print("\nWe found a bigger dinner table!\n")

names.insert(0, 'Jerry')
names.insert(2, 'Filip')
names.append('Soyhun')

for name in names:
    print(name+', you are invited to the dinner!')