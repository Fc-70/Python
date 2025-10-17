def create_adj_matrix(n, edges):
    matrix = [[0]*n for _ in range(n)]
    for u, v in edges:
        matrix[u][v] = 1
        matrix[v][u] = 1
    return matrix

def create_adj_list(n, edges):
    adj_list = [[] for _ in range(n)]
    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)
    return adj_list

def check_connection(matrix, u, v):
    return matrix[u][v] == 1

n = int(input("Enter total number of users: "))
m = int(input("Enter total number of connections: "))
edges = []
print("Enter connections (e.g., 0 1):")

for _ in range(m):
    u, v = map(int, input().split())
    edges.append((u, v))
adj_matrix = create_adj_matrix(n, edges)
adj_list = create_adj_list(n, edges)

print("\nAdjacency Matrix:")
for row in adj_matrix:
    print(row)
    
print("\nAdjacency List:")
for i in range(n):
    print(i, ":", adj_list[i])
    
u, v = map(int, input("\nEnter two users to check connection (e.g., 0 2): ").split())

if check_connection(adj_matrix, u, v):
    print(f"Users {u} and {v} are directly connected (friends).")
else:
    print(f"Users {u} and {v} are NOT directly connected.")
