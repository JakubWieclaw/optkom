import random
import netowrkx as nx


def egdes_reverse(G, a, b, c):

    G[a][b] = 1 - G[a][b]
    G[b][a] = 1 - G[b][a]

    G[a][c] = 1 - G[a][c]
    G[c][a] = 1 - G[c][a]

    G[b][c] = 1 - G[b][c]
    G[c][b] = 1 - G[c][b]

def check_graph(z_l, a, b, c):
    if ((a, b) in z_l) or ((a, c) in z_l) or ((b, c) in z_l) or ((b, a) in z_l) or ((c, a) in z_l) or ((c, b) in z_l):
        return True
    return False


def make_undirected_graph(n, pr):
    full_edges = (n-1)*n/2
    G = [[0]*n for _ in range(n)]
    cycle = list(range(n))
    random.shuffle(cycle)
    z_l = list(zip(cycle[:-1], cycle[1:]))
    for item in z_l:
        v = item[0]
        w = item[1]
        G[v][w] = 1
        G[w][v] = 1
    G[cycle[-1]][cycle[0]] = 1
    G[cycle[0]][cycle[-1]] = 1
    z_l.append((cycle[-1], cycle[0]))
    current_edges = n
    expected_edges = pr*full_edges
    while current_edges < expected_edges:
        a, b, c = random.sample(cycle, 3)
        if check_graph(z_l, a, b, c):
            continue
        s = G[a][b] + G[a][c] + G[b][c]
        if s > 1:
            continue
        else:
            egdes_reverse(G, a, b, c)
            current_edges += 3-s
    return G