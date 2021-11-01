from node import Node
import bisect

class Tree(object):
    def __init__(self, _minimumDegree):
        self.minimumDegree = _minimumDegree
        self.root = None

    def insert(self, keyToBeInserted):
        if not self.root:
            self.root = Node(self.minimumDegree, True)
            self.root.keys.append(keyToBeInserted)
            self.root.keyCount = 1
            return
        if self.root.keyCount + 1 == 2 * self.minimumDegree:
            newRoot = Node(self.minimumDegree, False)
            newRoot.children.append(self.root)
            newRoot.splitChild(0, self.root)
            i = 0
            if newRoot.keys[0] < keyToBeInserted:
                i+=1
            newRoot.children[i].insert(keyToBeInserted)
            self.root = newRoot
        else:
            self.root.insert(keyToBeInserted)