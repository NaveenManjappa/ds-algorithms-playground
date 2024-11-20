# Creating arrays in Python
# 1 Using List method
numbers = [10,20,30,40,50]

# 2 Using array module (specialized cases)
from array import array
marks = array('i',[76,89,67,97,92,91])
print(marks)


# Accessing elements O(1)
print(f"Numbers: {numbers}")
first_element = numbers[0]
last_element = numbers[-1]
print(f"First element: {first_element}")
print(f"Last element: {last_element}")

#Insertion - O(n) at worst case
numbers.append(60) # add to the end
numbers.insert(0,5) #add to the start
numbers.insert(2,15) #add to a particular index
print(f"Numbers after insertions: {numbers}")

# Deletion - O(n) at worst case
numbers.pop() # Remove last element
numbers.pop(0) # Remove element at index 0
numbers.pop(1) # Remove element at index 2
numbers.remove(50) # Remove first occurrence of value
print(f"Numbers after deletions: {numbers}")

# Updating elements - O(1)
numbers[0] = 5
print(f"Numbers after update: {numbers}")