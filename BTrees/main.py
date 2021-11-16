import math
import bisect
from tree import Tree

def getIntGreaterThan1(inputText):
    while True:
        try:
            n = int(input(inputText));
            if(n >= 1):
                return n
            else:
                raise Exception()
        except:
            print("Invalid Input. Expected inpur: Integer greater than 0")

minDegree = getIntGreaterThan1("Enter the min degree for BTree: ")
tree = Tree(math.ceil(minDegree/2))

while True:
    print("1. Insert Item\n2. Delete Item")
    print("3. Display Tree\n4. Exit")
    #try:
    choice = int(input("Enter choice: "))
    if(choice == 1):
        tree.insert(float(input("Enter the value to be inserted: ")))
    elif(choice == 2):
        tree.remove(float(input("Enter the value to be deleted: ")))
    elif(choice == 3):
        tree.traverse()
    elif(choice == 4):
        break
    else:
        raise Exception()
    #except:
       #print("Invalid Input.\n");
