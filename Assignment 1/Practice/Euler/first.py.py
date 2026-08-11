from collections import defaultdict

ip_name = input("Enter File name : ")

with open(ip_name, "r") as f:
    lines = f.readlines()

lines = [line.strip() for line in lines]

v, e = map(int, lines[0].split())

graph = defaultdict(list)

for i in range(1, e + 1):
    x, y = map(int, lines[i].split())
    graph[x].append(y)
    graph[y].append(x)


# Check whether graph is connected
visited = [False] * v

def dfs(vertex):
    visited[vertex] = True

    for adj in graph[vertex]:
        if not visited[adj]:
            dfs(adj)


# Find a vertex having at least one edge
start = -1

for i in range(v):
    if len(graph[i]) > 0:
        start = i
        break

if start != -1:
    dfs(start)


connected = True

for i in range(v):
    if len(graph[i]) > 0 and not visited[i]:
        connected = False
        break


# Check whether every vertex has even degree
even_degree = True

for i in range(v):
    if len(graph[i]) % 2 != 0:
        even_degree = False
        break


# Find Euler Tour
tour = []

def euler(vertex):
    while graph[vertex]:

        adj = graph[vertex].pop()

        # Remove the reverse edge
        graph[adj].remove(vertex)

        euler(adj)

    tour.append(vertex)


result = connected and even_degree and start != -1

if result:
    euler(start)
    tour.reverse()


op_name = input("Enter Output File Name : ")

with open(op_name, "w") as f:

    if result:
        f.write("Euler Tour exists\n")
        f.write(" -> ".join(map(str, tour)))
    else:
        f.write("Euler Tour does not exist")