import networkx as nx
from functions import Graph

astro = nx.read_edgelist("CA-AstroPh.txt", create_using=nx.Graph(), nodetype=int)
astro_graph = Graph(astro)

print('Результаты для графа CA-AstroPh:')
print('количество вершин: ', len(astro_graph.nodes))
print('количество ребер: ', len(astro_graph.edges))
print('плотность: ', astro_graph.density())
print('средний кластерный коэффициент: ', astro_graph.cluster_coef())
print('глобальный кластерный коэффициент: ', astro_graph.global_coef())
print('максимальная степень: ', astro_graph.max_degree())
print('минимальная степень: ', astro_graph.min_degree())
print('средняя степень: ', astro_graph.mean_degree())
astro_graph.show_probability_function()
astro_graph.show_log()
print('Количество треугольников:', astro_graph.triangles())
print('количество компонент слабой связности: ', astro_graph.weak_components())
print('доля вершин в максимальной по мощности компоненте слабой связности: ', astro_graph.weakly_comp_with_max_power())
print('оценка радиуса наибольшей компоненты слабой связности: ', astro_graph.radius())
print('оценка диаметра наибольшей компоненты слабой связности: ', astro_graph.diameter())
print('90 процентиль расстояния между вершинами наибольшей компоненты слабой связности: ', astro_graph.percentile_90())

print('Введите процент узлов, которые необходимо удалить из графа:')
x = int(input())
print('доля вершин в наибольшей компоненте слабой связности:', astro_graph.remove_x_perc(x))
print('Введите процент узлов, которые необходимо удалить из наибольшей степени:')
x = int(input())
print('доля вершин в наибольшей компоненте слабой связности:', astro_graph.remove_x_perc_max_degree(x))
print()

test = nx.read_edgelist("test.txt", create_using=nx.Graph(), nodetype=int)
component = list(max(nx.connected_components(test), key=len))
test_g = Graph(test)
print(test_g.distances_500(component))

google = nx.read_edgelist("web-Google.txt", create_using=nx.Graph(), nodetype=int)

di_google = nx.read_edgelist("web-Google.txt", create_using=nx.DiGraph(), nodetype=int)
print('граф считан')
meta = nx.condensation(di_google)
print(meta)
google_graph = Graph(google)
di_google_graph = Graph(google)
print('Результаты для графа web-Google:')
print('количество вершин: ', len(google_graph.nodes))
print('количество ребер: ', len(google_graph.edges))
print('плотность: ', google_graph.density())
print('средний кластерный коэффициент: ', google_graph.cluster_coef())
print('глобальный кластерный коэффициент: ', google_graph.global_coef())
print('максимальная степень: ', google_graph.max_degree())
print('минимальная степень: ', google_graph.min_degree())
print('средняя степень: ', google_graph.mean_degree())
google_graph.show_probability_function()
google_graph.show_log()
print('Количество треугольников:', google_graph.triangles())
print('количество компонент слабой связности: ', google_graph.weak_components())
print('количество компонент сильной связности: ', di_google_graph.strong_components())
print('доля вершин в максимальной по мощности компоненте слабой связности: ', google_graph.weakly_comp_with_max_power())
print('доля вершин в максимальной по мощности компоненте сильной связности: ', di_google_graph.strongly_comp_with_max_power())
di_google_graph.meta_graph()
component = list(max(nx.connected_components(google), key=len))
print(google_graph.distances_500(component))
print('оценка радиуса наибольшей компоненты слабой связности: ', google_graph.radius())
print('оценка диаметра наибольшей компоненты слабой связности: ', google_graph.diameter())
print('90 процентиль расстояния между вершинами наибольшей компоненты слабой связности: ', google_graph.percentile_90())

print('Введите процент узлов, которые необходимо удалить из графа:')
x = int(input())
print('доля вершин в наибольшей компоненте слабой связности:', google_graph.remove_x_perc(x))
print('Введите процент узлов, которые необходимо удалить из наибольшей степени:')
x = int(input())
print('доля вершин в наибольшей компоненте слабой связности:', google_graph.remove_x_perc_max_degree(x))
print()

vk = open('vk.csv', "r")
next(vk, None)
G = nx.parse_edgelist(vk, delimiter=',', create_using=nx.Graph(),
                      nodetype=int, data=(('t', float), ('h', float)))
vk_graph = Graph(G)
print('Результаты для графа vk:')
print('количество вершин: ', len(vk_graph.nodes))
print('количество ребер: ', len(vk_graph.edges))
print('плотность: ', vk_graph.density())
print('средний кластерный коэффициент: ', vk_graph.cluster_coef())
print('глобальный кластерный коэффициент: ', vk_graph.global_coef())
print('максимальная степень: ', vk_graph.max_degree())
print('минимальная степень: ', vk_graph.min_degree())
print('средняя степень: ', vk_graph.mean_degree())
vk_graph.show_probability_function()
vk_graph.show_log()
print('Количество треугольников:', vk_graph.triangles())
print('количество компонент слабой связности: ', vk_graph.weak_components())
print('доля вершин в максимальной по мощности компоненте слабой связности: ', vk_graph.weakly_comp_with_max_power())
print(vk_graph.distances_500())
print('оценка радиуса наибольшей компоненты слабой связности: ', vk_graph.radius())
print('оценка диаметра наибольшей компоненты слабой связности: ', vk_graph.diameter())
print('90 процентиль расстояния между вершинами наибольшей компоненты слабой связности: ', vk_graph.percentile_90())

print('Введите процент узлов, которые необходимо удалить из графа:')
x = int(input())
print('доля вершин в наибольшей компоненте слабой связности:', vk_graph.remove_x_perc(x))
print('Введите процент узлов, которые необходимо удалить из наибольшей степени:')
x = int(input())
print('доля вершин в наибольшей компоненте слабой связности:', vk_graph.remove_x_perc_max_degree(x))
x = input()

