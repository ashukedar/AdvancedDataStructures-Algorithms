from node import Node

class Tree(object):
    def getHeight(self, root):
        if not root:
            return 0
        return root.height
    
    def rightRotate(self, root):
        newRoot = root.left
        temp = newRoot.right
        newRoot.right = root
        root.left = temp
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        newRoot.height = 1 + max(self.getHeight(newRoot.left), self.getHeight(newRoot.right))
        return newRoot;

    def leftRotate(self, root):
        newRoot = root.right
        temp = newRoot.left
        newRoot.left = root
        root.right = temp
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        newRoot.height = 1 + max(self.getHeight(newRoot.left), self.getHeight(newRoot.right))
        return newRoot;

    def LL(self, root):
        return self.rightRotate(root)

    def RR(self, root):
        return self.leftRotate(root)
        
    def LR(self, root):
        root.left = self.leftRotate(root.left)
        return self.rightRotate(root)

    def RL(self, root):
        root.right = self.rightRotate(root.right)
        return self.leftRotate(root)

    def balanceTree(self, root, newItemKey):
        balanceFactor = self.getHeight(root.left) - self.getHeight(root.right)
        if balanceFactor > 1 and root.left.value > newItemKey:
            return self.LL(root)
        elif balanceFactor < -1 and root.right.value < newItemKey:
            return self.RR(root)
        elif balanceFactor > 1 and root.left.value < newItemKey:
            return self.LR(root)
        elif balanceFactor < -1 and root.right.value > newItemKey:
            return self.RL(root)
        return root;
    
    def insert(self, root, newItemKey):
        if not root:
            return Node(newItemKey)
        elif root.value == newItemKey:
            print("This key already exists.")
        elif root.value > newItemKey:
            root.left = self.insert(root.left, newItemKey)
        else:
            root.right = self.insert(root.right, newItemKey)
        root.height = 1 + max(self.getHeight(root.left), 
                              self.getHeight(root.right))
        return self.balanceTree(root, newItemKey)
    
    def getMinValueChild(self, root):
        if not root or not root.left:
            return root
        return self.getMinValueChild(root.left)

    def delete(self, root, keyToBeDeleted):
        if not root:
            print("Key not found");
            return None;
        elif root.value > keyToBeDeleted:
            root.left = self.delete(root.left, keyToBeDeleted)
        elif root.value < keyToBeDeleted:
            root.right = self.delete(root.right, keyToBeDeleted)
        else:
            if not root.left:
                temp = root.right;
                root = None
                return temp
            elif not root.right:
                temp = root.left
                root = None
                return temp
            temp = self.getMinValueChild(root.right)
            temp.left = root.left
            root = temp
        
        root.height = 1 + max(self.getHeight(root.left), 
                              self.getHeight(root.right))
        return self.balanceTree(root, keyToBeDeleted)