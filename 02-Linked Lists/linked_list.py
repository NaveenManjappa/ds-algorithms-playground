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
        if self.first is None:
            raise IndexError("Cannot remove from an Empty list")

        if self.first == self.last:
            self.first = self.last = None
            return

        second = self.first.next_node
        self.first.next_node = None
        self.first = second

    def delete_last(self):
        if self.first is None:
            raise IndexError("Cannot remove from an Empty list")

        if self.first == self.last:
            self.first = self.last = None
            return

        previous = self._get_previous_node(self.last)
        last = previous
        last.next_node = None

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

    def display(self):
        current = self.first

        while current is not None:
            print(f"{ current.value}",end=" ")
            current = current.next_node
        print()
