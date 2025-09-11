names = ['Jerry','Marcello','Filip', 'Seyeon', 'Marie','Soyhun']
print("Unfortunately, we can only invite two people for dinner.\n")
while len(names) > 2:
    removed_guest = names.pop()
    print("Sorry, "+removed_guest+", we can't invite you to dinner.")

print("\nYou are still invited, ")
for name in names:
    print(name+", you are still invited to dinner.")

del names[0]
del names[0]

print("\nFinal guest list:", names)