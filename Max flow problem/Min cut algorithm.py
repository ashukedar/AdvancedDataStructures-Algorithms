from collections import defaultdict

class Graph:

	def __init__(self,graph):
		self.graph = graph
		self.org_graph = [i[:] for i in graph]
		self. ROW = len(graph)
		self.COL = len(graph[0])

	def BFS(self,s, t, parent):
		visited =[False]*(self.ROW)

		queue=[]
		queue.append(s)
		visited[s] = True

		while queue:
			u = queue.pop(0)
			for ind, val in enumerate(self.graph[u]):
				if visited[ind] == False and val > 0 :
					queue.append(ind)
					visited[ind] = True
					parent[ind] = u

		return True if visited[t] else False
		
	def dfs(self, graph,s,visited):
		visited[s]=True
		for i in range(len(graph)):
			if graph[s][i]>0 and not visited[i]:
				self.dfs(graph,i,visited)

	def minCut(self, source, sink):
		parent = [-1]*(self.ROW)
		max_flow = 0
		while self.BFS(source, sink, parent) :
			path_flow = float("Inf")
			s = sink
			while(s != source):
				if path_flow >= self.graph[parent[s]][s]:
					path_flow = self.graph[parent[s]][s]
				s = parent[s]
			
			max_flow += path_flow
			v = sink
			while(v != source):
				u = parent[v]
				self.graph[u][v] -= path_flow
				self.graph[v][u] += path_flow
				v = parent[v]

		visited=len(self.graph)*[False]
		self.dfs(self.graph,s,visited)

		for i in range(self.ROW):
			for j in range(self.COL):
				if self.graph[i][j] == 0 and self.org_graph[i][j] > 0 and visited[i]:
					print(str(i) + " - " + str(j))

graph = [[0, 16, 13, 0, 0, 0],
		[0, 0, 10, 12, 0, 0],
		[0, 4, 0, 0, 14, 0],
		[0, 0, 9, 0, 0, 20],
		[0, 0, 0, 7, 0, 4],
		[0, 0, 0, 0, 0, 0]]

g = Graph(graph)

source = 0; sink = 5

g.minCut(source, sink)