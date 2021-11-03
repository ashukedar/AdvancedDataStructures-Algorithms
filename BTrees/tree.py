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

    def traverse(self):
        print("Tree current state: ")
        if not self.root:
            return
        self.root.traverse(0)
        print("")

    def remove(self, keyToBeDeleted):
        node = self.search(keyToBeDeleted)
        if not node:
            return;
        node.remove(keyToBeDeleted)
        if self.root.keyCount == 0:
            temp = self.root
            if self.root.isLeaf:
                self.root = None
            else:
                self.root = self.root.children[0]
            del temp;
