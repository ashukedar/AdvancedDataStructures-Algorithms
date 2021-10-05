import math

class FibonacciTree:
    def __init__(self, value):
        self.value = value
        self.children = []
        self.order = 0

    def add_at_end(self, t):
        self.children.append(t)
        self.order = self.order + 1
        
    def display(self, count):
        print(self.value, end='')
        for i in range(len(self.children)):
            for j in range(count):
                print("\t", end='')
            self.children[i].display(count+1)
            print()

class FibonacciHeap:
    def __init__(self):
        self.trees = []
        self.least = None
        self.count = 0

    def insert(self, value):
        new_tree = FibonacciTree(value)
        self.trees.append(new_tree)
        if (self.least is None or value < self.least.value):
            self.least = new_tree
        self.count += 1

    def get_min(self):
        if self.least is None:
            return None
        return self.least.value

    def extract_min(self):
        smallest = self.least
        if smallest is not None:
            for child in smallest.children:
                self.trees.append(child)
            self.trees.remove(smallest)
            if self.trees == []:
                self.least = None
            else:
                self.least = self.trees[0]
                self.consolidate()
            self.count = self.count - 1
            return smallest.value

    def consolidate(self):
        aux = (floor_log(self.count) + 1) * [None]

        while self.trees != []:
            x = self.trees[0]
            order = x.order
            self.trees.remove(x)
            while aux[order] is not None:
                y = aux[order]
                if x.value > y.value:
                    x, y = y, x
                x.add_at_end(y)
                aux[order] = None
                order = order + 1
            aux[order] = x

        self.least = None
        for k in aux:
            if k is not None:
                self.trees.append(k)
                if (self.least is None
                        or k.value < self.least.value):
                    self.least = k

    def display(self):
        for i in range(len(self.trees)):
            print('Tree', i+1)
            self.trees[i].display(1)
            print('\n')

def floor_log(x):
    return math.frexp(x)[1] - 1

fibonacci_heap = FibonacciHeap()
while True:
    try:
        print('1. Insert\n2. Min get\n3. Min extract\n4. Display\n5. Exit')
        operation = int(input('What would you like to do? '))
        if operation == 1:
            fibonacci_heap.insert(int(input("Enter the data to be inserted: ")))
            print("Inserted successfully!")
        elif operation == 2:
            print('Minimum value:', fibonacci_heap.get_min())
        elif operation == 3:
            print('Minimum value remove:', fibonacci_heap.extract_min())
            print("Removed successfully!")
        elif operation == 4:
            fibonacci_heap.display()
        elif operation == 5:
            break
        else:
           raise Exception()
    except:
         print("Invalid Input.\n");