from functions import Graph, DiGraph


def import_graph(name):
    graph = open(name, "r")
    if name == 'vk.csv':
        next(graph, None)
    n = []
    e = []
    with graph as file:
        for line in file:
            if '#' not in line:
                if name == 'vk.csv':
                    u, v, t, h = line.split(',')
                else:
                    u, v = line.split()
                n.append(u)
                n.append(v)
                e.append((u, v))
    return n, e


n, e = import_graph('CA-AstroPh.txt')
astro_graph = Graph(n, e)

print('Результаты для графа CA-AstroPh:')
print('количество вершин: ', astro_graph.count_nodes())
print('количество ребер: ', astro_graph.count_edges())
print('плотность: ', astro_graph.density())
print('средний кластерный коэффициент: ', astro_graph.cluster_coef())
print('глобальный кластерный коэффициент: ', astro_graph.global_coef())
print('максимальная степень: ', astro_graph.max_degree())
print('минимальная степень: ', astro_graph.min_degree())
print('средняя степень: ', astro_graph.mean_degree())
astro_graph.show_probability_function()
astro_graph.show_log()
print('Количество треугольников:', astro_graph.triangles())
print('количество компонент слабой связности: ', astro_graph.number_weakly_components())
print('доля вершин в максимальной по мощности компоненте слабой связности: ',
      astro_graph.nodes_in_weakly_comp_with_max_power())
print('оценка радиуса наибольшей компоненты слабой связности: ', astro_graph.radius())
print('оценка диаметра наибольшей компоненты слабой связности: ', astro_graph.diameter())
print('90 процентиль расстояния между вершинами наибольшей компоненты слабой связности: ', astro_graph.percentile())

print('Введите процент узлов, которые необходимо удалить из графа:')
x = int(input())
print('доля вершин в наибольшей компоненте слабой связности:', astro_graph.remove_x_perc(x))
print('Введите процент узлов наибольшей степени, которые необходимо удалить:')
x = int(input())
print('доля вершин в наибольшей компоненте слабой связности:', astro_graph.remove_x_perc_max_degree(x))
print()


n, e = import_graph('web-Google.txt')
google_graph = Graph(n, e)
di_google_graph = DiGraph(n, e)

print('Результаты для графа web-Google:')
print('количество вершин: ', google_graph.count_nodes())
print('количество ребер: ', google_graph.count_edges())
print('плотность: ', google_graph.density())
print('средний кластерный коэффициент: ', google_graph.cluster_coef())
print('глобальный кластерный коэффициент: ', google_graph.global_coef())
print('максимальная степень: ', google_graph.max_degree())
print('минимальная степень: ', google_graph.min_degree())
print('средняя степень: ', google_graph.mean_degree())
google_graph.show_probability_function()
google_graph.show_log()
print('Количество треугольников:', google_graph.triangles())
print('количество компонент слабой связности: ', google_graph.number_weakly_components())
print('количество компонент сильной связности: ', di_google_graph.number_strongly_components())
print('доля вершин в максимальной по мощности компоненте слабой связности: ', google_graph.nodes_in_weakly_comp_with_max_power())
print('доля вершин в максимальной по мощности компоненте сильной связности: ', di_google_graph.nodes_in_strongly_comp_with_max_power())
print('Мета граф: ', di_google_graph.meta_graph())
print('оценка радиуса наибольшей компоненты слабой связности: ', google_graph.radius())
print('оценка диаметра наибольшей компоненты слабой связности: ', google_graph.diameter())
print('90 процентиль расстояния между вершинами наибольшей компоненты слабой связности: ', google_graph.percentile())

print('Введите процент узлов, которые необходимо удалить из графа:')
x = int(input())
print('доля вершин в наибольшей компоненте слабой связности:', google_graph.remove_x_perc(x))
print('Введите процент узлов наибольшей степени, которые необходимо удалить:')
x = int(input())
print('доля вершин в наибольшей компоненте слабой связности:', google_graph.remove_x_perc_max_degree(x))
print()

n, e = import_graph('vk.csv')
vk_graph = Graph(n, e)
print('Результаты для графа vk:')
print('количество вершин: ', vk_graph.count_nodes())
print('количество ребер: ', vk_graph.count_edges())
print('плотность: ', vk_graph.density())
print('средний кластерный коэффициент: ', vk_graph.cluster_coef())
print('глобальный кластерный коэффициент: ', vk_graph.global_coef())
print('максимальная степень: ', vk_graph.max_degree())
print('минимальная степень: ', vk_graph.min_degree())
print('средняя степень: ', vk_graph.mean_degree())
vk_graph.show_probability_function()
vk_graph.show_log()
print('Количество треугольников:', vk_graph.triangles())
print('количество компонент слабой связности: ', vk_graph.number_weakly_components())
print('доля вершин в максимальной по мощности компоненте слабой связности: ', vk_graph.nodes_in_weakly_comp_with_max_power())
print('оценка радиуса наибольшей компоненты слабой связности: ', vk_graph.radius())
print('оценка диаметра наибольшей компоненты слабой связности: ', vk_graph.diameter())
print('90 процентиль расстояния между вершинами наибольшей компоненты слабой связности: ', vk_graph.percentile())

print('Введите процент узлов, которые необходимо удалить из графа:')
x = int(input())
print('доля вершин в наибольшей компоненте слабой связности:', vk_graph.remove_x_perc(x))
print('Введите процент узлов наибольшей степени, которые необходимо удалить:')
x = int(input())
print('доля вершин в наибольшей компоненте слабой связности:', vk_graph.remove_x_perc_max_degree(x))
print()
