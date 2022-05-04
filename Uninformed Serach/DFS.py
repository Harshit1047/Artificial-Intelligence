import sys
class ShortestPath:
def __init__(self, start, end):
self.start = start
self.end = end
self.shortLength = sys.maxsize
def findPath(self):
self.dfs(self.start)
self.trace_route()
def dfs(self, vertex):
global length
length +=1
if length &gt; self.shortLength:
return
if vertex == self.end:
self.shortLength = length
return
visited[vertex] = 1
#iterate through all unvisited neighbors vertices
for i in range(N):

if adjacencyM[vertex][i] == 1 and visited[i] == 0:
nbr = i
prev[nbr] = vertex
self.dfs(nbr)
length -=1
def trace_route(self):
vertex = self.end
route = []
while vertex != -1:
route.append(vertices_names[vertex])
vertex = prev[vertex]
route.reverse()
print(route)
if __name__ == &#39;__main__&#39;:
#vertices or nodes
vertices_names = [&#39;A&#39;, &#39;B&#39;, &#39;C&#39;, &#39;D&#39;, &#39;E&#39;];
#number of vertices
N = len(vertices_names)
#Adjacency Matrix
adjacencyM = [[0, 1, 0, 0, 0],
[1, 0, 1, 0, 1],
[0, 1, 0, 1, 1],
[0, 0, 1 ,0, 1],
[0, 1, 0, 1, 0]];
#List mapping of vertices to mark them visited
visited = [0 for x in range(N)]
#List to stores preceding vertices
prev = [-1 for x in range(N)]
#Driver code
sp = ShortestPath(0, 4)
length = 0
sp.findPath()
