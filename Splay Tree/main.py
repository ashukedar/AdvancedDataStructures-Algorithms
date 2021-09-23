from SplayTree import Tree

def preOrderDisplay(root):
    if not root:
        return;
    list1.append(root.value)
    preOrderDisplay(root.left)
    preOrderDisplay(root.right)
    
def inOrderDisplay(root):
    if not root:
        return;
    inOrderDisplay(root.left)
    list2.append(root.value)
    inOrderDisplay(root.right)
    
def postOrderDisplay(root):
    if not root:
        return;
    postOrderDisplay(root.left)
    postOrderDisplay(root.right)
    list3.append(root.value)

def display():
    list1.clear()
    list2.clear()
    list3.clear()
    preOrderDisplay(root)
    inOrderDisplay(root)
    postOrderDisplay(root)
    print("Preorder:", list1)
    print("Inorder:", list2)
    print("Postorder:", list3, "\n")

list1 = []
list2 = []
list3 = []
root = None
tree = Tree()

while True:
    print("1. Insert Item \n2. Delete Item")
    print("3. Search Item\n4. Display Tree\n5. Exit")
    try:
        choice = int(input("Enter choice: "))
        if(choice == 1):
            root = tree.insert(root, int(input("Enter the value to be inserted: ")))
        elif(choice == 2):
            root = tree.delete(root, int(input("Enter the value to be deleted: ")))
        elif(choice == 3):
            root = tree.search(root, int(input("Enter the value to be searched: ")))
        elif(choice == 4):
            display()
        elif(choice == 5):
            break
        else:
            raise Exception()
    except:
        print("Invalid Input.\n");