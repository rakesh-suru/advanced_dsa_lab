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

visited = [False] * v


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


visited[0] = True
path = [0]


result = hamiltonian_cycle(0, 0, path)

op_name = input("Enter Output File Name :")

with open(op_name, "w") as f:

    if result:
        f.write("Hamiltonian Cycle exists\n")
        f.write(" -> ".join(map(str, path)))
    else:
        f.write("Hamiltonian Cycle does not exist")
