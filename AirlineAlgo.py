import random

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    def addEdge(self, u, v, w):
        self.graph[u][v] = w
        self.graph[v][u] = w

    def printSolution(self, dist):
        print("Vertex \t Distance from Source")
        for node in range(self.V):
            print(node, "\t\t", dist[node])

    def minDistance(self, dist, sptSet):
        min = float("inf")
        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v
        return min_index

    def dijkstra(self, src, dest):
        dist = [float("inf")] * self.V
        dist[src] = 0
        sptSet = [False] * self.V
        for cout in range(self.V):
            u = self.minDistance(dist, sptSet)
            sptSet[u] = True
            for v in range(self.V):
                if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]
        self.printSolution(dist)
        if dist[dest] != float("inf"):
            print(f"The shortest distance from {src+1} to {dest+1} is {dist[dest]}")
        else:
            print("Not possible")

numTerminals = int(input("Enter the number of terminals: "))
graph = Graph(numTerminals)

for i in range(1, numTerminals + 1):
    for j in range(i + 1, numTerminals + 1):
        # randomly decide whether there's an edge between terminal i and j
        if random.choice([True, False]):
            weight = int(input(f"Enter the weight between terminal {i} and {j}: ")or random.randint(1, 100))
            graph.addEdge(i-1, j-1, weight)

src = int(input("Enter the source terminal: "))
dest = int(input("Enter the destination terminal: "))
graph.dijkstra(src-1, dest-1)
