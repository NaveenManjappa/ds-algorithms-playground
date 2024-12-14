class Stack:
    def __init__(self):
        self.items = [0] * 5
        self.count = 0

    def push(self,item):
        if self.count == len(self.items):
            raise Exception("Stack is full")
        self.items[self.count] = item
        self.count += 1

    def is_empty(self):
        return self.count == 0

    def pop(self):
        if self.count == 0:
            raise Exception("Stack is empty")

        self.count -= 1

    def peek(self):
        if self.count == 0:
            raise Exception("Stack is empty!")

        return self.items[self.count-1]

    def display(self):
        print(f"Stack: {self.items[:self.count]}")
