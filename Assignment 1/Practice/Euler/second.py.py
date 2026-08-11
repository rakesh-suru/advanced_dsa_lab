from collections import defaultdict

ip_name = input("Enter File name : ")

with open(ip_name, "r") as f:
    lines = f.readlines()

lines = [line.strip() for line in lines]

i = 0
graph_no = 1
results = []


# Euler Tour using DFS
def euler(vertex, graph, tour):

    while graph[vertex]:

        adj = graph[vertex].pop()

        # Remove the reverse edge
        graph[adj].remove(vertex)

        euler(adj, graph, tour)

    tour.append(vertex)


# Check whether graph is connected
def is_connected(graph, v):

    visited = [False] * v

    # Find a vertex having at least one edge
    start = -1

    for vertex in range(v):
        if len(graph[vertex]) > 0:
            start = vertex
            break

    # Graph with no edges
    if start == -1:
        return True

    def dfs(vertex):
        visited[vertex] = True

        for adj in graph[vertex]:
            if not visited[adj]:
                dfs(adj)

    dfs(start)

    # Every vertex having an edge must be visited
    for vertex in range(v):
        if len(graph[vertex]) > 0 and not visited[vertex]:
            return False

    return True


while i < len(lines):

    # Skip blank lines
    if lines[i] == "":
        i += 1
        continue

    # Number of vertices and edges
    v, e = map(int, lines[i].split())
    i += 1

    graph = defaultdict(list)

    # Read edges
    for j in range(e):
        x, y = map(int, lines[i].split())

        graph[x].append(y)
        graph[y].append(x)

        i += 1

    # Check even degree
    even_degree = True

    for vertex in range(v):
        if len(graph[vertex]) % 2 != 0:
            even_degree = False
            break

    # Check connectivity
    connected = is_connected(graph, v)

    result = even_degree and connected

    if result:

        # Make a copy because Euler algorithm removes edges
        euler_graph = defaultdict(list)

        for vertex in graph:
            euler_graph[vertex] = graph[vertex].copy()

        # Find starting vertex
        start = 0

        for vertex in range(v):
            if len(euler_graph[vertex]) > 0:
                start = vertex
                break

        tour = []

        euler(start, euler_graph, tour)

        tour.reverse()

        # Make sure all edges were used
        if len(tour) == e + 1:
            results.append(
                "Graph " + str(graph_no) + ":\n"
                "Euler Tour exists\n"
                + " -> ".join(map(str, tour))
            )
        else:
            results.append(
                "Graph " + str(graph_no) + ":\n"
                "Euler Tour does not exist"
            )

    else:
        results.append(
            "Graph " + str(graph_no) + ":\n"
            "Euler Tour does not exist"
        )

    graph_no += 1


op_name = input("Enter Output File Name : ")

with open(op_name, "w") as f:

    for result in results:
        f.write(result)
        f.write("\n\n")