# Common Array operations
from operator import index

my_list = [10,20,30,40,50,20]

# Length
length = len(my_list)
print(f"Length: {length}")

# Slicing
sub_array = my_list[1:4] ## elements from index 1 to 3
print(f"Sub Array: {sub_array}")

# Searching
#index = my_list.index(200) # not in list error
# index = my_list.index(20)
index = 0
if 20 in my_list:
    index = my_list.index(20) # Find index of first occurrence of the element

print(f"Searching: {index}")

# Sorting
my_list.sort() # in-place sorting
print(f"In place Sorting: {my_list}")

sorted_list = sorted(my_list) # Create new sorted list
print(f"New Sorted list: {sorted_list}")

# Reversing
my_list.reverse() # In place reversing
print(f"In place reversal: {my_list}")

reversed_list = my_list[::-1] # create new reversed list
print(f"New Reversed list: {reversed_list}")