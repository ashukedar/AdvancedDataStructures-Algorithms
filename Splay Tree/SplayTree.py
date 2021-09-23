from Node import Node

class Tree(object):
    def rightRotate(self, root):
        newRoot = root.left
        temp = newRoot.right
        newRoot.right = root
        root.left = temp
        return newRoot

    def leftRotate(self, root):
        newRoot = root.right
        temp = newRoot.left
        newRoot.left = root
        root.right = temp
        return newRoot
        
    def splay(self, root, key):
        if not root or root.value == key:
            return root
        if root.value > key:
            if not root.left:
                return root
            if root.left.value > key:     #Zig Zig
                root.left.left = self.splay(root.left.left, key)
                root = self.rightRotate(root)
            elif root.left.value < key:   #Zig Zag
                root.left.right = self.splay(root.left.right, key)
                if root.left.right:
                    root = self.leftRotate(root)
            if not root.left:
                return root
            else:
                return self.rightRotate(root)
        else:
            if not root.right:
                return root
            if root.right.value > key:     #Zag Zig
                root.right.left = self.splay(root.right.left, key)
                if root.right.left:
                    root.right = self.rightRotate(root.right)
            elif root.right.value < key:   #Zag Zag
                root.right.right = self.splay(root.right.right, key)
                root = self.leftRotate(root)
            if not root.right:
                return root
            else:
                return self.leftRotate(root)
        
    def insert(self, root, valueToBeInserted):
        if not root:
            return Node(valueToBeInserted);
        root = self.splay(root, valueToBeInserted)
        if root.value == valueToBeInserted:
            return root;
        newRoot = Node(valueToBeInserted)
        if root.value > valueToBeInserted:
            newRoot.right = root
            newRoot.left = root.left
            root.left = None
        else:
            newRoot.left = root
            newRoot.right = root.right
            root.right = None
        return newRoot
    
    def search(self, root, valueToBeSearched):
        newRoot = self.splay(root, valueToBeSearched)
        if not newRoot or newRoot.value != valueToBeSearched:
            print("Value not present in the tree")
        else:
            print("Value is been shifted to root")
        return newRoot

    def getMinValueChild(self, root):
        if not root or not root.left:
            return root
        return self.getMinValueChild(root.left)
    
    def delete(self, root, valueToBeDeleted):
        newRoot = self.splay(root, valueToBeDeleted)
        if not newRoot or newRoot.value != valueToBeDeleted:
            print("Value not present in the tree")
            return newRoot
        if not newRoot.left:
            temp = newRoot.right;
            newRoot = None
            return temp
        if not newRoot.right:
            temp = newRoot.left
            newRoot = None
            return temp
        temp = self.getMinValueChild(newRoot.right)
        temp.left = newRoot.left
        return temp