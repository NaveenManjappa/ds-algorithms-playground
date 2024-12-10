from stack import Stack

stack = Stack()

my_string = "abcd"
for c in my_string:
    stack.push(c)

reversed_string =''
for c in my_string:
    reversed_string += stack.pop()

print(f"Reversed string: {reversed_string}")



