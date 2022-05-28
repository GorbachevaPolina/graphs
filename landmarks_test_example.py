import networkx as nx
from functions import Graph
import random
import time

n = []
e = []
with open('CA-AstroPh.txt', 'r') as file:
    for line in file:
        if '#' not in line:
            u, v = line.split()
            n.append(u)
            n.append(v)
            e.append((u, v))
astro_graph = Graph(n, e)

astro = nx.read_edgelist("CA-AstroPh.txt", create_using=nx.Graph(), nodetype=int)

landmarks = astro_graph.select_landmarks_by_coverage(50, 100)

print('5 LANDMARKS:')

distances, trees = astro_graph.count_distances(landmarks[:5])

error_basic = 0; error_sc = 0; time_basic = 0; time_sc = 0

for _ in range(500):
    node_1 = random.choice(list(astro_graph.nodes))
    node_2 = random.choice(list(astro_graph.nodes))

    try: path_lib = len(nx.shortest_path(astro, source=int(node_1), target=int(node_2))) - 1
    except: path_lib = 1e9

    time_start = time.time()
    distance_basic = astro_graph.landmarks_basic(node_1, node_2, distances)
    time_end = time.time()
    time_basic = time_basic + time_end - time_start

    error_basic += (distance_basic - path_lib)/path_lib

    time_start = time.time()
    distance_sc = astro_graph.landmarks_sc(node_1, node_2, trees)
    time_end = time.time()
    time_sc = time_sc + time_end-time_start

    error_sc += (distance_sc - path_lib) / path_lib

print('AVERAGE time basic: ', time_basic/500)
print('AVERAGE time sc: ', time_sc/500)

print('FINAL error basic: ', error_basic/500)
print('FINAL error sc: ', error_sc/500)
