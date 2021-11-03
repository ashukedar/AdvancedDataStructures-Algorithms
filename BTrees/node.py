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

    def remove(self, keyToBeDeleted):
        if self.isLeaf:
            self.keys.remove(keyToBeDeleted)
            self.keyCount-=1
            return
        index = self.keys.index(keyToBeDeleted)
        if self.children[index].keyCount >= self.minimumDegree:
            prev = self.getPrev(index)
            self.keys[index] = prev
            self.children[index].search(prev).remove(prev)
        elif self.children[index+1].keyCount >= self.minimumDegree:
            succ = self.getSucc(index)
            self.keys[index] = succ
            self.children[index+1].search(succ).remove(succ)
        else:
            self.merge(index)
            self.children[index].search(keyToBeDeleted).remove(keyToBeDeleted)

    def fill(self, index):
        if self.children[index].keyCount < self.minimumDegree:
            if index != 0 and self.children[index-1].keyCount >= self.minimumDegree:
                print("1", self.keys)
                self.borrowFromPrev(index)
            elif index != self.keyCount and self.children[index].keyCount >= self.minimumDegree:
                print("2", self.keys)
                self.borrowFromNext(index)
            elif index != self.keyCount:
                print("3", self.keys)
                self.merge(index)
            else:
                print("4", self.keys)
                self.merge(index-1)
    
    def borrowFromNext(self, index):
        child = self.children[index]
        sibling = self.children[index+1]

        child.keys.append(self.keys[index])
        self.keys.remove(self.keys[index])
        self.keys.insert(index, sibling.keys[0])
        sibling.remove(sibling.keys[0])
        
        child.children.append(sibling.children[0])
        sibling.remove(sibling.children[0])

        child.keyCount += 1
        sibling.keyCount -= 1

    def borrowFromPrev(self, index):
        child = self.children[index]
        sibling = self.children[index-1]

        child.keys.insert(0, self.keys[index])
        self.keys.remove(self.keys[index])
        self.keys.insert(index, sibling.keys[sibling.keyCount-1])
        sibling.remove(sibling.keys[sibling.keyCount-1])
        
        child.children.insert(0, sibling.children[sibling.keyCount-1])
        sibling.remove(sibling.children[sibling.keyCount-1])        

        child.keyCount += 1
        sibling.keyCount -= 1

    def getPrev(self, index):
        curr = self.children[index]
        while not curr.isLeaf:
                curr = curr.children[-1]
        return curr.keys[-1]

    def getSucc(self, index):
        curr = self.children[index+1]
        while not curr.isLeaf:
            curr = curr.children[0]
        return curr.keys[0]        

    def merge(self, index):
        child = self.children[index]
        sibling = self.children[index+1]

        child.keys.append(self.keys[index])
        for i in range(sibling.keyCount):
            child.keys.append(sibling.keys[i])
        if not child.isLeaf:
            for i in range(sibling.keyCount):
                child.children.append(self.children[i])
        for i in range(index+1, self.keyCount):
            self.keys[i-1] = self.keys[i]
        for i in range(index+2, self.keyCount+1):
            self.children[i-1] = self.children[i]
        child.keyCount += sibling.keyCount + 1
        self.keys.remove(self.keys[index])
        self.keyCount -= 1
        del sibling