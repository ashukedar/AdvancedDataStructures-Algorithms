import sys

def maxInt():
    return 1000

class Graph():    
	def __init__(self, vertices):
		self.V = vertices
		self.graph = [[0 for column in range(vertices)]
					for row in range(vertices)]

	def printSolution(self, dist):
		print("Vertex \tDistance from Source")
		for node in range(self.V):
			print(node, "\t\t", dist[node])

	def minDistance(self, dist, sptSet):
		min = maxInt()
		for u in range(self.V):
			if dist[u] < min and sptSet[u] == False:
				min = dist[u]
				min_index = u
		return min_index

	def dijkstra(self, src):
		dist = [maxInt()] * self.V
		dist[src] = 0
		sptSet = [False] * self.V

		for cout in range(self.V):
			x = self.minDistance(dist, sptSet)
			sptSet[x] = True
			for y in range(self.V):
				if self.graph[x][y] > 0 and sptSet[y] == False and \
				dist[y] > dist[x] + self.graph[x][y]:
						dist[y] = dist[x] + self.graph[x][y]

		self.printSolution(dist)

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

def getFloat(inputText):
    while True:
        try:
            return float(input(inputText));
        except:
            print("Invalid Input. Expected input: Float")

v = getIntGreaterThan1("Enter the no. of vertices: ")
e = getIntGreaterThan1("Enter the no. of edges: ")
g = Graph(v)
for i in range(v):
    g.graph.append([0] * v)
for i in range(e):
    vertex1 = getIntGreaterThan1("Enter the vertex1 of edge " + str(i+1) + ": ")
    vertex2 = getIntGreaterThan1("Enter the vertex2 of edge " + str(i+1) + ": ")
    value = getIntGreaterThan1("Enter the value of edge " + str(i+1) + ": ")
    g.graph[vertex1-1][vertex2-1] = value
    g.graph[vertex2-1][vertex1-1] = value

g.dijkstra(0);