my_marks = { 'Maths':98, 'Science':94,'English':90 }

#Assign a value
my_marks[None] = 124
my_marks['Kannada'] = 456
my_marks['Kannada'] = 120 #it overrides the existing value for the key

#Keys are case-sensitive
my_marks['kannada'] = 122 #it creates a new key

#Get the length
print(f"Length: {len(my_marks)}")

#Iterate through the keys
for key in my_marks:
    print(key)

#Look for a key existence
if "Maths" in my_marks:
    print("Key exists")

#Look for value existence
my_marks['Social'] = 98
if 98 in my_marks.values():
    print("Value exists")

#Iterate over key-value pairs
for (key,value) in my_marks.items():
    print(f"Key: {key}, Value: {value}")

#Find all the keys for a specified value
print([key for key,value in my_marks.items() if value == 98]) #list comprehension

del my_marks['kannada']
print(my_marks)

