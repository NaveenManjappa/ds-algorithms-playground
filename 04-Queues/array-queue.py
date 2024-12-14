class ArrayQueue:
    front, rear,count = 0,0,0

    def __init__(self,length):
        self.queue = [0] * length

    def enqueue(self,item):
        if self.count == len(self.queue):
            raise Exception("Queue is full")

        self.queue[self.rear] = item
        self.rear = (self.rear + 1) % len(self.queue)
        self.count += 1

    def dequeue(self):
        if self.count == 0:
            raise Exception("Queue is Empty")

        item = self.queue[self.front]
        self.queue[self.front]=0
        self.front = (self.front + 1) % len(self.queue)
        self.count -= 1
        return item

    def peek(self):
        return self.queue[self.front]

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == len(self.queue)

    def display(self):
        print(self.queue)


array_queue = ArrayQueue(5)
array_queue.enqueue(10)
array_queue.enqueue(20)
array_queue.enqueue(30)
array_queue.enqueue(40)
array_queue.enqueue(50)
array_queue.dequeue()
array_queue.dequeue()
array_queue.enqueue(60)
array_queue.enqueue(70)
array_queue.dequeue()


array_queue.display()
print(array_queue.peek())
