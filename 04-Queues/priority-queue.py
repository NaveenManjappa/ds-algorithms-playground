class PriorityQueue:
    items = []
    front = 0
    count = 0

    def enqueue(self,item):
        if self.is_empty():
            self.items.append(item)
            self.count += 1
            return

        counter = len(self.items)-1
        for i in range(counter,-1,-1):
            #print(i,item)
            if self.items[i] > item:
                if self.is_full(i):
                    self.extend_array()
                    self.items[i+1] = self.items[i]
                else:
                    self.items[i+1]=self.items[i]
            else:
                if self.is_full(i):
                    self.extend_array()
                    self.items[i + 1] = item
                    self.count += 1
                    break
                else:
                    self.items[i+1] = item
                    self.count += 1
                    break

    def extend_array(self):
        self.items.extend([0] * 1)

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty!")
        else:
            ret = self.items[self.front]
            self.front += 1
            self.count -= 1
            return ret

    def is_empty(self):
        return self.count == 0

    def is_full(self,i):
        return i + 1 >= len(self.items)

    def display(self):
        print(f"Priority Queue:{self.items}")

p_queue = PriorityQueue()
p_queue.enqueue(1)
p_queue.enqueue(3)
p_queue.enqueue(5)
p_queue.enqueue(2)
p_queue.display()
print(p_queue.dequeue())
print(p_queue.dequeue())
print(p_queue.dequeue())
print(p_queue.dequeue())
