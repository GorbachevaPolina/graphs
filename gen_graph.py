import networkx as nx
from itertools import combinations, groupby
import random


def gnp_random_connected_graph(v, p):
    edges = combinations(range(v), 2)
    G = nx.Graph()
    G.add_nodes_from(range(v))
    if p <= 0:
        return G
    if p >= 1:
        return nx.complete_graph(v, create_using=G)
    for _, node_edges in groupby(edges, key=lambda x: x[0]):
        node_edges = list(node_edges)
        random_edge = random.choice(node_edges)
        G.add_edge(*random_edge)
        for e in node_edges:
            if random.random() < p:
                G.add_edge(*e)
    return G