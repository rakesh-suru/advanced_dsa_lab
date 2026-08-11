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
all_cycles = []


def hamiltonian_cycle(start, curr, path):

    if len(path) == v:

        if start in graph[curr]:
            all_cycles.append(path[:] + [start])

        return

    for adj in graph[curr]:

        if not visited[adj]:

            visited[adj] = True
            path.append(adj)

            hamiltonian_cycle(start, adj, path)

            path.pop()
            visited[adj] = False


visited[0] = True
path = [0]

hamiltonian_cycle(0, 0, path)

op_name = input("Enter Output File Name : ")

with open(op_name, "w") as f:

    if all_cycles:
        f.write("Hamiltonian Cycles exist\n\n")

        for i, cycle in enumerate(all_cycles, 1):
            f.write(f"Cycle {i}: ")
            f.write(" -> ".join(map(str, cycle)))
            f.write("\n")

    else:
        f.write("Hamiltonian Cycle does not exist\n")