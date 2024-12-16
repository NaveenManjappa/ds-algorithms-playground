class PriorityQueue:
    items = []

    def enqueue(self,item):
        if len(self.items) == 0:
            self.items.append(item)
            return

        j = len(self.items)-1
        for i in range(j,-1,-1):
            print(i,item)
            if self.items[i] > item:
                if i+1 >= len(self.items):
                    self.items.extend([0]*1)
                    #print(self.items)
                    self.items[i+1] = self.items[i]
                    #print(self.items)
                else:
                    self.items[i+1]=self.items[i]
            else:
                if i + 1 >= len(self.items):
                    self.items.extend([0] * 1)
                    self.items[i + 1] = item
                    print(self.items,item)
                    break
                else:
                    self.items[i+1] = item
                    break


    def display(self):
        print(f"Priority Queue:{self.items}")

p_queue = PriorityQueue()
p_queue.enqueue(1)
p_queue.enqueue(3)
p_queue.enqueue(5)
p_queue.display()
p_queue.enqueue(2)
p_queue.display()