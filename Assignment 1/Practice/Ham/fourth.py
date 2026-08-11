from collections import defaultdict

ip_name = input("Enter File name : ")

with open(ip_name, "r") as f:
    lines = f.readlines()

lines = [line.strip() for line in lines]

i = 0
graph_no = 1
results = []


def hamiltonian_cycle(start, curr, mask, path, graph, v, memo):

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

            new_mask = mask | (1 << adj)

            if hamiltonian_cycle(start, adj, new_mask,
                                 path, graph, v, memo):
                return True

            path.pop()

    memo[(curr, mask)] = False

    return False


while i < len(lines):

    if lines[i] == "":
        i += 1
        continue

    v, e = map(int, lines[i].split())
    i += 1

    graph = defaultdict(list)

    for j in range(e):
        x, y = map(int, lines[i].split())

        graph[x].append(y)
        graph[y].append(x)

        i += 1

    memo = {}

    path = [0]

    mask = 1 << 0

    result = hamiltonian_cycle(
        0, 0, mask, path, graph, v, memo
    )

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