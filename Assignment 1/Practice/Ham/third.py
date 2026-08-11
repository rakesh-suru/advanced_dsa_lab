from collections import defaultdict

ip_name = input("Enter File name : ")

with open(ip_name, "r") as f:
    lines = f.readlines()

lines = [line.strip() for line in lines]

i = 0
graph_no = 1
results = []


def hamiltonian_cycle(start, curr, path):

    if len(path) == v:
        if start in graph[curr]:
            path.append(start)
            return True
        return False

    for adj in graph[curr]:

        if not visited[adj]:

            visited[adj] = True
            path.append(adj)

            if hamiltonian_cycle(start, adj, path):
                return True

            path.pop()
            visited[adj] = False

    return False


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

    visited = [False] * v
    path = [0]

    visited[0] = True

    result = hamiltonian_cycle(0, 0, path)

    if result:
        results.append(
            f"Graph {graph_no}: Hamiltonian Cycle exists\n"
            f"Cycle: {' -> '.join(map(str, path))}\n"
        )
    else:
        results.append(
            f"Graph {graph_no}: Hamiltonian Cycle does not exist\n"
        )

    graph_no += 1


op_name = input("Enter Output File Name : ")

with open(op_name, "w") as f:
    f.write("\n".join(results))

print("Output written to", op_name)
