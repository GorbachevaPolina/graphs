import networkx as nx
from functions import Graph

test = nx.read_edgelist("socfb-Middlebury45.txt", create_using=nx.Graph(), nodetype=int)
test_graph = Graph(test)

# Эти функции не проверяла
print('количество вершин: ', len(test_graph.nodes))
print('количество ребер: ', len(test_graph.edges))
print('плотность: ', test_graph.density())
print('средний кластерный коэффициент: ', test_graph.cluster_coef())
print('глобальный кластерный коэффициент: ', test_graph.global_coef())
print('максимальная степень: ', test_graph.max_degree())
print('минимальная степень: ', test_graph.min_degree())
print('средняя степень: ', test_graph.mean_degree())
# test_graph.show_probability_function()
# test_graph.show_log()
print('Количество треугольников:', test_graph.triangles())

# Связность и расстояния, все проверила
print('количество компонент слабой связности: ', test_graph.number_weakly_components())
print('ПРОВЕРКА количество компонент слабой связности: ', nx.number_connected_components(test))
print('доля вершин в максимальной по мощности компоненте слабой связности: ',
      len(test_graph.weakly_comp_with_max_power()) / len(test_graph.nodes))
print('ПРОВЕРКА доля вершин в максимальной по мощности компоненте слабой связности: ',
      len(max(nx.connected_components(test), key=len)) / test.number_of_nodes())
print('оценка радиуса наибольшей компоненты слабой связности: ', test_graph.radius())
print('оценка диаметра наибольшей компоненты слабой связности: ', test_graph.diameter())
print('90 процентиль расстояния между вершинами наибольшей компоненты слабой связности: ', test_graph.percentile())


# Удаление вершин, работает кстати долговато, на самом большои графе на 75% наиб. степени 1.5 минуты
# print('Удаление случайных узлов: ')
# print('доля вершин в наибольшей компоненте слабой связности:', test_graph.remove_x_perc(25) / len(test_graph.nodes))
#
# print('Удаление узлов наибольшей степени: ')
# print('доля вершин в наибольшей компоненте слабой связности:', test_graph.remove_x_perc_max_degree(75)
#       / len(test_graph.nodes))


# Функции для ориентированных графов
# Ориентированные: email-Eu-core.txt, soc-wiki-Vote.txt
test = nx.read_edgelist("soc-wiki-Vote.txt", create_using=nx.DiGraph(), nodetype=int)
test_graph = Graph(test)

print('количество компонент сильной связности: ', test_graph.number_strongly_components())
print('доля вершин в максимальной по мощности компоненте сильной связности: ',
      len(test_graph.strongly_comp_with_max_power()) / len(test_graph.nodes))
print('Мета граф: ', test_graph.meta_graph())
print('ПРОВЕРКА количество компонент сильной связности: ', nx.number_strongly_connected_components(test))
print('ПРОВЕРКА доля вершин в максимальной по мощности компоненте сильной связности: ',
      len(max(nx.strongly_connected_components(test), key=len)) / test.number_of_nodes())
print('ПРОВЕРКА Мета граф: ', nx.condensation(test))
