my_list = [10,20,30,40,50]

# Different ways to use Slice notation
sub_array = my_list[1:4]
print(f"Sub array 1-3: {sub_array}")

print(my_list)

print(f"Move forward by 2: {my_list[::2]}")
print(f"Move backward one position: {my_list[::-1]}")
print(f"Index 0 to 3: {my_list[0:3:1]}")
print(my_list)
print(f"Index 3 to 0: {my_list[3::-1]}")

word = "radar"
is_palindrome = word == word[::-1]
print(f"Is Palindrome?: {is_palindrome}")