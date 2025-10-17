def add_edge(graph, u, v):
    graph[u].append(v)
    graph[v].append(u)
    
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    traversal = []
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            traversal.append(node)
            for neighbour in graph[node]:
                if neighbour not in visited:
                    queue.append(neighbour)
    return traversal

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    traversal = [start]
    for neighbour in graph[start]:
        if neighbour not in visited:
            traversal.extend(dfs(graph, neighbour, visited))
    return traversal

n = int(input("Enter number of vertices: "))
graph = {i: [] for i in range(n)}

e = int(input("Enter number of edges: "))
print("Enter each edge (e.g., 0 1):")
for _ in range(e):
    u, v = map(int, input().split())
    add_edge(graph, u, v)
    
print("\nGraph Representation (Adjacency List):")
for node in graph:
    print(node, ":", graph[node])
    
start = int(input("\nEnter starting vertex for traversal: "))

print("\nBreadth First Search (BFS) traversal:")
print(bfs(graph, start))

print("\nDepth First Search (DFS) traversal:")
print(dfs(graph, start))
