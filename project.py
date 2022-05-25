import networkx as nx
from functions import Graph
from gen_graph import generate_graph



astro = nx.read_edgelist("CA-AstroPh.txt", create_using=nx.Graph(), nodetype=int)
astro_graph = Graph(astro)


print('Результаты для первого графа:')
print('количество вершин: ', len(astro_graph.nodes))
print('количество ребер: ', len(astro_graph.edges))
print('плотность: ', astro_graph.density())
print('средний кластерный коэффициент: ', astro_graph.cluster_coef())
print('глобальный кластерный коэффициент: ', astro_graph.global_coef())
print('максимальная степень: ', astro_graph.max_degree())
print('минимальная степень: ', astro_graph.min_degree())
print('средняя степень: ', astro_graph.mean_degree())
astro_graph.show_probability_function()
astro_graph.show_hist()
astro_graph.show_log()
print('Количество треугольников:', astro_graph.triangles())

google = nx.read_edgelist("web-Google.txt", create_using=nx.Graph(), nodetype=int)
google_graph = Graph(google)
print('Результаты для второго графа:')
print('количество вершин: ', len(google_graph.nodes))
print('количество ребер: ', len(google_graph.edges))
print('плотность: ', google_graph.density())
print('средний кластерный коэффициент: ', google_graph.cluster_coef())
print('глобальный кластерный коэффициент: ', google_graph.global_coef())
print('максимальная степень: ', google_graph.max_degree())
print('минимальная степень: ', google_graph.min_degree())
print('средняя степень: ', google_graph.mean_degree())
google_graph.show_probability_function()
google_graph.show_hist()
google_graph.show_log()
print('Количество треугольников:', google_graph.triangles())

vk = open('vk.csv', "r")
next(vk, None)
G = nx.parse_edgelist(vk, delimiter=',', create_using=nx.Graph(),
                      nodetype=int, data=(('t', float), ('h', float)))
vk_graph = Graph(G)
print('Результаты для третьего графа:')
print('количество вершин: ', len(vk_graph.nodes))
print('количество ребер: ', len(vk_graph.edges))
print('плотность: ', vk_graph.density())
print('средний кластерный коэффициент: ', vk_graph.cluster_coef())
print('глобальный кластерный коэффициент: ', vk_graph.global_coef())
print('максимальная степень: ', vk_graph.max_degree())
print('минимальная степень: ', vk_graph.min_degree())
print('средняя степень: ', vk_graph.mean_degree())
vk_graph.show_probability_function()
vk_graph.show_hist()
vk_graph.show_log()
print('Количество треугольников:', vk_graph.triangles())

