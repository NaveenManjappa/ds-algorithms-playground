class Array:
    def __init__(self): #constructor
        self.list = [] # Create an instance-specific list

    def insert(self,item):
        self.list.append(item)

    def remove_at(self,index):
        self.list.pop(index)

    def index_of(self,value):
        return self.list.index(value)

    def display(self):
        print(f"Array list: {self.list}")

sample = Array()
sample.insert(1)
sample.insert(2)
sample.insert(3)
sample.insert(4)
sample.remove_at(0)
sample.display()
print(f"Index of 3: {sample.index_of(3)}")

