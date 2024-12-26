colors = { 'red','green','blue' }

colors.add('black')
colors.add('black')
colors.remove('black') #Raises KeyError if not found
colors.discard('black1') #Does not raise KeyError if not found
print(colors)

empty_set = set()
print("red" in colors)

set1 = { 1,2,3,4 }
set2 = { 3,4,5,6 }
print(set1 | set2 ) #Union
print(set1 & set2) #Intersection
print(set1 - set2) #Elements present in Set1 but not in Set2

text = "Hello World"
print(set(text))