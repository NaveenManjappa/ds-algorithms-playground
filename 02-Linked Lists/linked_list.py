from typing import Optional
class LinkedList:

    def __init__(self):
       self.first : Optional[Node] = None
       self.last :Optional[Node] = None

    def add_first(self,value):
        node = Node(value,None)

        if self.first is None:
           self.first = node
           self.last = node
        else:
            node.next_node = self.first
            self.first = node

    def add_last(self,value):
        node = Node(value,None)

        if self.first is None:
            self.last = self.first = node
        else:
            self.last.next_node = node
            self.last = node

    def delete_first(self):
        self.first = self.first.next_node

    def delete_last(self):
        node = self.first
        if node.next_node is None:
            self.first = None
            self.last = None

        while node.next_node is not None and node.next_node != self.last:
            node = node.next_node

        self.last = node
        node.next_node = None

    def contains(self,value):
        node = self.first

        if self.first.value == value or self.last.value == value:
            return True

        if self.first.next_node is None:
            return False

        while node.next_node is not None:
            node = node.next_node
            if node.value == value:
                return True

        return False

    def index_of(self,value):
        node = self.first

        if self.first.value == value:
            return 0

        index = 0
        while node.next_node is not None:
            node = node.next_node
            index += 1
            if node.value == value:
                return index

        if self.last.value == value:
            index += 1
            return index

        return -1

    def display(self):
        node = self.first

        if node.next_node is None:
            print(f"Elements are: {node.value} ")
            return

        while node.next_node is not None:
            print(f"{ node.value}",end=" ")
            node = node.next_node

        print(self.last.value)

class Node:
    def __init__(self,value,next_node):
        self.value = value
        self.next_node = next_node