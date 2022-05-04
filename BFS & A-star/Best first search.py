from queue import PriorityQueue
import matplotlib.pyplot as plt
import networkx as nx
# for implementing BFS | returns path having lowest cost
def best_first_search(source, target, n):
  visited = [0] * n
  visited[source] = True
  pq = PriorityQueue()
  pq.put((0, source))
  while pq.empty() == False:
    u = pq.get()[1]
    print(u, end=" ") # the path having lowest cost
    if u == target:
       break
    for v, c in graph[u]:
      if visited[v] == False:
         visited[v] = True
         pq.put((c, v))
  print()
# for adding edges to graph
def addedge(x, y, cost):
  graph[x].append((y, cost))
  graph[y].append((x, cost))
G = nx.Graph()
v = int(input("Enter the number of nodes: "))
graph = [[] for i in range(v)] # undirected Graph
e = int(input("Enter the number of edges: "))
print("Enter the edges along with their weights:")
for i in range(e):
  x, y, z = list(map(int, input().split()))
  addedge(x, y, z)
  G.add_edge(x, y, weight = z)
source = int(input("Enter the Source Node: "))
target = int(input("Enter the Target/Destination Node: "))
print("\nPath: ", end = "")
best_first_search(source, target, v)
print("Graph:\n")
pos = nx.spring_layout(G, seed=7) # positions for all nodes - seed for reproducibility
# nodes
nx.draw_networkx_nodes(G, pos, node_size=350)
# edges
nx.draw_networkx_edges(G, pos)
nx.draw_networkx_edges(G, pos, alpha=0.5, edge_color="r")
# labels
nx.draw_networkx_labels(G, pos, font_size=20)
ax = plt.gca()
ax.margins(0.08)
plt.axis("off")
plt.tight_layout()
plt.show()
