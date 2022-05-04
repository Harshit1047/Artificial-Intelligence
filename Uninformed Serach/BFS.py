def add_edge(adj, src, dest):
adj[src].append(dest);
adj[dest].append(src);
def BFS(adj, src, dest, v, pred, dist):
queue = []
visited = [False for i in range(v)];
for i in range(v):
dist[i] = 1000000
pred[i] = -1;
visited[src] = True;
dist[src] = 0;
queue.append(src);
while (len(queue) != 0):
u = queue[0];
queue.pop(0);
for i in range(len(adj[u])):
if (visited[adj[u][i]] == False):
visited[adj[u][i]] = True;
dist[adj[u][i]] = dist[u] + 1;
pred[adj[u][i]] = u;
queue.append(adj[u][i]);
if (adj[u][i] == dest):
return True;

return False;
def printShortestDistance(adj, s, dest, v):
pred=[0 for i in range(v)]
dist=[0 for i in range(v)];
if (BFS(adj, s, dest, v, pred, dist) == False):

print(&quot;Given source and destination are not connected&quot;)
path = []
crawl = dest;
crawl = dest;
path.append(crawl);
while (pred[crawl] != -1):
path.append(pred[crawl]);
crawl = pred[crawl];

print(&quot;Shortest path length is : &quot; + str(dist[dest]), end = &#39;&#39;)
print(&quot;\nPath is : : &quot;)
for i in range(len(path)-1, -1, -1):
print(path[i], end=&#39; &#39;)
if __name__==&#39;__main__&#39;:
v = 8;
adj = [[] for i in range(v)];
add_edge(adj, 0, 1);
add_edge(adj, 0, 3);
add_edge(adj, 1, 2);
add_edge(adj, 3, 4);
add_edge(adj, 3, 7);
add_edge(adj, 4, 5);
add_edge(adj, 4, 6);
add_edge(adj, 4, 7);
add_edge(adj, 5, 6);
add_edge(adj, 6, 7);
add_edge(adj, 2, 6);
source = 0
dest = 6;
printShortestDistance(adj, source, dest, v);
