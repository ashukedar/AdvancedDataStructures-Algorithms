import bisect 

class Node(object):
    def __init__(self, _minimumDegree, _isLeaf):
        self.keys = []
        self.minimumDegree = _minimumDegree
        self.children = []
        self.keyCount = 0
        self.isLeaf = _isLeaf

    def insert(self, keyToBeInserted):
        i = self.keyCount - 1
        if self.isLeaf:
            self.keys.insert(bisect.bisect_left(self.keys, keyToBeInserted), 
                             keyToBeInserted)
            self.keyCount+=1
            return
        while i >= 0 and self.keys[i] > keyToBeInserted:
            i-=1
        if self.children[i+1].keyCount + 1 > 2 * self.minimumDegree - 1:
            self.splitChild(i+1, self.children[i+1])
            if self.keys[i+1] < keyToBeInserted:
                i+=1
        self.children[i+1].insert(keyToBeInserted)

    def splitChild(self, index, node):
        newNode = Node(node.minimumDegree, node.isLeaf)
        newNode.keyCount = self.minimumDegree - 1
        for i in range(self.minimumDegree-1):
            newNode.keys.append(node.keys[i+self.minimumDegree])
        if not node.isLeaf:
            for i in range(self.minimumDegree):
                newNode.children.append(node.children[i+self.minimumDegree])
        node.keyCount = self.minimumDegree - 1
        self.children.insert(index+1, newNode)
        self.keys.insert(index, node.keys[self.minimumDegree-1])
        del node.keys[node.keyCount: len(node.keys)]
        if not self.isLeaf:
            del node.children[node.keyCount+1: len(node.children)]
        self.keyCount += 1
        
    def traverse(self, depth):
        for i in range(self.keyCount):
            if not self.isLeaf:
                self.children[i].traverse(depth+1)
            for j in range(depth):
                 print("\t", end="")
            print(self.keys[i], end =" ")
            if not self.isLeaf:
                print()
        print()
        if not self.isLeaf:
            self.children[self.keyCount].traverse(depth+1)