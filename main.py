import networkx



number_of_cannibals = 3
number_of_researches = 3
number_of_sides = 2

start_idx = end_idx = 0
nodes = []
for c in range(number_of_cannibals+1):
    for r in range(number_of_researches+1):
        for c2 in range(number_of_cannibals+1):
            for r2 in range(number_of_researches+1):
                for s in range(number_of_sides):
                    if ((c + r +c2 + r2) == 6 and (c + c2) == 3):
                        if s == 0 and c2 > r2:
                            continue
                        if s == 1 and c > r:
                            continue
                        nodes.append((c,r,c2,r2,s))
                        if c == 3 and r == 3 and s == 0:
                            start_idx = len(nodes) -1
                        if c2 == 3 and r2 == 3 and s == 1:
                            end_idx = len(nodes) -1


print(len(nodes))

G = networkx.DiGraph()
for idx,node in enumerate(nodes):
    G.add_node(idx)
for idx1, node_a in enumerate(nodes):
    for idx2, node_b in enumerate(nodes):
        if idx1 != idx2 and \
                (node_a[4] != node_b[4] and
                ((node_a[0] + node_a[1] - node_b[0] - node_b[1]) in [1,2] and node_a[4] == 0 or ((node_a[2] + node_a[3] - node_b[2] - node_b[3]) in [1,2]) and node_a[4] == 1)):
            G.add_edge(idx1, idx2)

fw = networkx.shortest_path(G, source=start_idx, target=end_idx, weight=None, method='dijkstra')
for n in fw:
    print(nodes[n])