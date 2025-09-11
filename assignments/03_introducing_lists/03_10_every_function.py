things = ['Chinese', 'American', 'French', 'Japanese', 'Spanish']

print(things)
things[1]
things.append('Korean')
things.insert(0, 'Italian') 
things.remove('French')
things.pop()
del things[2]

print("sorted(temp): ", sorted(things))
print("sorted reverse(temp): ", sorted(things, reverse=True))
things.sort()
things.reverse()
print("final list", things)
