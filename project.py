import networkx as nx
from functions import Graph
from gen_graph import gnp_random_connected_graph

astro = nx.read_edgelist("CA-AstroPh.txt", create_using=nx.Graph(), nodetype=int)
astro_graph = Graph(astro)

print('количество вершин: ', len(astro_graph.nodes))
print('количество ребер: ', len(astro_graph.edges))
print('плотность: ', astro_graph.density())
print('средний кластерный коэффициент: ', astro_graph.cluster_coef())
print('глобальный кластерный коэффициент: ', astro_graph.global_coef())
print('макисмальная степень: ', astro_graph.max_degree())
print('минимальная степень: ', astro_graph.min_degree())
print('средняя степень: ', astro_graph.mean_degree())
astro_graph.show_probability_function()
astro_graph.show_hist()
astro_graph.show_log()
print('Количество треугольников:', astro_graph.triangles())

# google = nx.read_edgelist("web-Google.txt", create_using=nx.Graph(), nodetype=int)
# google_graph = Graph(google)

# vk = open('vk.csv', "r")
# next(vk, None)
# G = nx.parse_edgelist(vk, delimiter=',', create_using=nx.Graph(),
#                       nodetype=int, data=(('t', float), ('h', float)))
