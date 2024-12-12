from queue import Queue

def reverse_queue(queue):
    reversed_queue = Queue()
    stack = []

    while not queue.empty():
        stack.append(queue.get())


    while stack:
        reversed_queue.put(stack.pop())

    return reversed_queue

q = Queue()
q.put(10)
q.put(20)
q.put(30)
print(list(q.queue))

reversed_q = reverse_queue(q)


while not reversed_q.empty():
    print(reversed_q.get(),end=" ")
