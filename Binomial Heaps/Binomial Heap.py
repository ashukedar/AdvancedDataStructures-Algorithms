class BinomialTree:
    def __init__(self, key):
        self.key = key
        self.children = []
        self.order = 0

    def add_at_end(self, t):
        self.children.append(t)
        self.order = self.order + 1

    def display(self):
        print(self.key, end='')
        for i in range(len(self.children)):
            print("\t", end='')
            self.children[i].display()
            print()

class BinomialHeap:
    def __init__(self):
        self.trees = []
    
    def extract_min(self):
        if self.trees == []:
            return None
        smallest_node = self.trees[0]
        for tree in self.trees:
            if tree.key < smallest_node.key:
                smallest_node = tree
        self.trees.remove(smallest_node)
        h = BinomialHeap()
        h.trees = smallest_node.children
        self.merge(h)
        return smallest_node.key
    
    def get_min(self):
        if self.trees == []:
            return None
        least = self.trees[0].key
        for tree in self.trees:
            if tree.key < least:
                least = tree.key
        return least

    def merge(self, h):
        self.trees.extend(h.trees)
        self.trees.sort(key=lambda tree: tree.order)
        if len(self.trees) == 0:
            return
        i = 0
        while i < len(self.trees) - 1:
            current = self.trees[i]
            after = self.trees[i + 1]
            if current.order == after.order:
                if i + 2 < len(self.trees) and self.trees[i + 2].order == after.order:
                    after_after = self.trees[i + 2]
                    if after.key < after_after.key:
                        after.add_at_end(after_after)
                        del self.trees[i + 2]
                    else:
                        after_after.add_at_end(after)
                        del self.trees[i + 1]
                else:
                    if current.key < after.key:
                        current.add_at_end(after)
                        del self.trees[i + 1]
                    else:
                        after.add_at_end(current)
                        del self.trees[i]
            i+=1
 
    def insert(self, key):
        temp = BinomialHeap()
        temp.trees.append(BinomialTree(key))
        self.merge(temp)
        
    def display(self):
        for i in range(len(self.trees)):
            self.trees[i].display()
            print()

bheap = BinomialHeap()
while True:
    trees = bheap.trees
    try:
        print('1. Insert\n2. Min get\n3. Min extract\n4. Display\n5. Exit')
        operation = int(input('What would you like to do? '))
        if operation == 1:
            bheap.insert(int(input("Enter the data to be inserted: ")))
            print("Inserted successfully!")
        elif operation == 2:
            print('Minimum value:', bheap.get_min())
        elif operation == 3:
            print('Minimum value remove:', bheap.extract_min())
            print("Removed successfully!")
        elif operation == 4:
            bheap.display();
        elif operation == 5:
            break
        else:
           raise Exception()
    except:
         print("Invalid Input.\n");