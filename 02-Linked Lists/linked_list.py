from operator import indexOf
from typing import Optional

class Node:
    def __init__(self,value,next_node):
        self.value = value
        self.next_node = next_node

class LinkedList:

    def __init__(self):
       self.first : Optional[Node] = None
       self.last :Optional[Node] = None
       self.size = 0

    def add_first(self,value):
        node = Node(value,None)

        if self.first is None:
           self.first = node
           self.last = node
        else:
            node.next_node = self.first
            self.first = node
        self.size +=1

    def add_last(self,value):
        node = Node(value,None)

        if self.first is None:
            self.last = self.first = node
        else:
            self.last.next_node = node
            self.last = node
        self.size += 1

    def delete_first(self):
        if self.first is None:
            raise IndexError("Cannot remove from an Empty list")

        if self.first == self.last:
            self.first = self.last = None
        else:
            second = self.first.next_node
            self.first.next_node = None
            self.first = second

        self.size -= 1

    def delete_last(self):
        if self.first is None:
            raise IndexError("Cannot remove from an Empty list")

        if self.first == self.last:
            self.first = self.last = None
        else:
            previous = self._get_previous_node(self.last)
            last = previous
            last.next_node = None

        self.size -= 1

    def _get_previous_node(self,node:Node):
        current = self.first
        while current is not None:
            if current.next_node == node:
                return current
            else:
                current=current.next_node
        return None

    def contains(self,item):
        return self.index_of(item) != -1

    def index_of(self,item):
        index = 0
        current = self.first
        while current is not None:
            if current.value == item:
                return index
            current = current.next_node
            index += 1

        return -1

    def list_size(self):
        return self.size

    def to_array(self):
        array = []
        current = self.first
        while current is not None:
            array.append(current.value)
            current = current.next_node
        return array

    def reverse(self):
        current = self.first
        previous = None

        while current is not None:
            next_node = current.next_node
            current.next_node = previous
            previous = current
            current = next_node

        self.first = previous


    def display(self):
        current = self.first

        while current is not None:
            print(f"{ current.value}",end=" ")
            current = current.next_node
        print()
