def getIntGreaterThan1(inputText):
    while True:
        try:
            n = int(input(inputText));
            if(n >= 1):
                return n
            else:
                raise Exception()
        except:
            print("Invalid Input. Expected input: Integer greater than 0")

def unionFind(curr, search):
    if edges[curr][search]:
        edges[curr][search] = False
        edges[0][search] = True
        return True
    for i in range(n):
        if edges[curr][i] and unionFind(i, search):
            edges[curr][i] = False
            edges[0][i] = True
            return True
    return False

def getEdges():
    print("Current state of edges:")
    for edge in edges:
        print(edge)

def find(search):
    if unionFind(0, search):
        print("Node found")
    else:
        print("Node not found")

n = getIntGreaterThan1("Enter the no. of vertices: ")
e = getIntGreaterThan1("Enter the no. of edges: ")
edges = []
for i in range(n):
    arr = []
    for j in range(n):
        arr.append(False)
    edges.append(arr)

for i in range(e):
    v1 = getIntGreaterThan1("Enter the no. of vertex 1 for edge " + str(i+1) + ": ") - 1
    v2 = getIntGreaterThan1("Enter the no. of vertex 2 for edge " + str(i+1) + ": ") - 1    
    edges[v1][v2] = True

while True:
    try:
        print('1. Find\n2. Display Edges\n3. Exit')
        operation = int(input('What would you like to do? '))
        if operation == 1:
            find(getIntGreaterThan1("Enter the node to be search: ") - 1)
        elif operation == 2:
            getEdges()
        elif operation == 3:
            break
        else:
           raise Exception()
    except:
         print("Invalid Input.\n");