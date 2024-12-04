from operator import indexOf
from tokenize import endpats
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
        if self.first is None:
            return

        current = self.first
        previous = None
        while current is not None:
            next_node = current.next_node
            current.next_node = previous
            previous = current
            current = next_node

        self.last = self.first
        self.last.next_node = None
        self.first = previous

    def get_kth_node_from_end(self, k):

        if k <0 or k > self.list_size() or self.first is None:
            return
        # 1. Need two pointers that are k-1 distance apart
        # 2. Traverse until the second pointer reaches the end
        # 3. Return the value of first pointer

        first_pointer = self.first
        second_pointer = self.first
        index =1

        # for i in range(0,k-1):
        #     second_pointer = second_pointer.next_node
        #     if second_pointer is None: # this indicates k is larger than size of the linked list
        #         return

        while second_pointer != self.last:
            if index < k:
                second_pointer = second_pointer.next_node
            else:
                second_pointer = second_pointer.next_node
                first_pointer = first_pointer.next_node
            index += 1

        return first_pointer.value


    def display(self):
        current = self.first
        while current is not None:
            print(f"{ current.value}",end=" ")
            current = current.next_node
        print()
