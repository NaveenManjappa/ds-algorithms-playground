from stack import Stack

def is_balanced_expression(expr):
    stack = Stack()

    for char in expr:
        #print(char)
        if char == '(' or char == '[' or char == '<':
            stack.push(char)

        if char == ')' or char == ']' or char == '>':
            top = stack.pop()
            #print(pop_char)
            if char == ')' and top != '(':
                return False
            if char == '>' and top != '<':
                return False
            if char == ']' and top != '[':
                return False

    return stack.is_empty()

my_expr = "(<a>+(b))"

print(f"Result: {is_balanced_expression(my_expr)}")


