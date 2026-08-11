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


start = 0

memo = {}


def hamiltonian_cycle(curr, mask, path):

    if mask == (1 << v) - 1:

        if start in graph[curr]:
            path.append(start)
            return True

        return False

    if (curr, mask) in memo:
        return False

    for adj in graph[curr]:

        if not (mask & (1 << adj)):

            path.append(adj)

            if hamiltonian_cycle(adj, mask | (1 << adj), path):
                return True

            path.pop()

    memo[(curr, mask)] = False

    return False


path = [start]

result = hamiltonian_cycle(start, 1 << start, path)


op_name = input("Enter Output File Name : ")

with open(op_name, "w") as f:

    if result:
        f.write("Hamiltonian Cycle exists\n")
        f.write(" -> ".join(map(str, path)))
    else:
        f.write("Hamiltonian Cycle does not exist")
