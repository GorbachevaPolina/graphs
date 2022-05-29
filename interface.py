from functions import Graph, DiGraph
import random


def import_graph(name):
    graph = open(name, "r")
    n = set()
    e = []
    with graph as file:
        for line in file:
            if '#' not in line:
                u, v = line.split()
                n.add(u)
                n.add(v)
                e.append((u, v))
    return n, e


print('Введите название файла, в котором находится тестовый граф (с расширением):')
test_file = input()

n, e = import_graph(test_file)
test_graph = Graph(n, e)

print('Нажмите номер функции, которую необходимо вызвать:')
print('1. Число вершин')
print('2. Число ребер')
print('3. Плотность')
print('4. Число  компонент  слабой связности')
print('5. Доля вершин в наибольшей компоненте слабой связности')
print('6. Число  компонент  сильной связности')
print('7. Доля вершин в наибольшей компоненте сильной связности')
print('8. Оценка радиуса')
print('9. Оценка диаметра')
print('10. Оценка 90 процентиля')
print('11. Построить мета-граф')
print('12. Количество треугольников')
print('13. Средний кластерный коэффициент')
print('14. Глобальный кластерный коэффициент')
print('15. Минимальная степень узла графа')
print('16. Средняя степень узла графа')
print('17. Максимальная степень узла графа')
print('18. Функция вероятности')
print('19. Функция вероятности в log-log шкалах')
print('20. Удалить случайным образом x% узлов')
print('21. Удалить x% узлов наибольшей степени')
print('22. Посчитать расстояние между двумя вершинами')
a = int(input())
if a == 1:
    print('Количество вершин: ', test_graph.count_nodes())
elif a == 2:
    print('Количество ребер: ', test_graph.count_edges())
elif a == 3:
    print('Плотность: ', test_graph.density())
elif a == 4:
    print('Количество компонент слабой связности: ', test_graph.number_weakly_components())
elif a == 5:
    print('Доля вершин в наибольшей компоненте слабой связности: ', test_graph.nodes_in_weakly_comp_with_max_power())
elif a == 6:
    if test_file == 'email-Eu-core.txt' or test_file == 'soc-wiki-Vote.txt':
        di_test_graph = DiGraph(n, e)
        print('Количество компонент сильной связности: ', di_test_graph.number_strongly_components())
    else:
        print('Граф неориентированный')
elif a == 7:
    if test_file == 'email-Eu-core.txt' or test_file == 'soc-wiki-Vote.txt':
        di_test_graph = DiGraph(n, e)
        print('Доля вершин в наибольшей компоненте сильной связности: ', di_test_graph.nodes_in_strongly_comp_with_max_power())
    else:
        print('Граф неориентированный')
elif a == 8:
    print('Оценка радиуса наибольшей компоненты слабой связности: ', test_graph.radius())
elif a == 9:
    print('Оценка диаметра наибольшей компоненты слабой связности: ', test_graph.diameter())
elif a == 10:
    print('90 процентиль расстояния наибольшей компоненты слабой связности: ', test_graph.percentile())
elif a == 11:
    if test_file == 'email-Eu-core.txt' or test_file == 'soc-wiki-Vote.txt':
        di_test_graph = DiGraph(n, e)
        meta = di_test_graph.meta_graph()
        print('Мета граф: число вершин - ', meta.count_nodes(), ', число ребер - ', meta.count_edges())
    else:
        print('Граф неориентированный')
elif a == 12:
    print('Количество треугольников:', test_graph.triangles())
elif a == 13:
    print('Средний кластерный коэффициент: ', test_graph.cluster_coef())
elif a == 14:
    print('Глобальный кластерный коэффициент: ', test_graph.global_coef())
elif a == 15:
    print('Минимальная степень: ', test_graph.min_degree())
elif a == 16:
    print('Средняя степень: ', test_graph.mean_degree())
elif a == 17:
    print('Максимальная степень: ', test_graph.max_degree())
elif a == 18:
    test_graph.show_probability_function()
elif a == 19:
    test_graph.show_log()
elif a == 20:
    print('Введите процент узлов, которые необходимо удалить из графа:')
    x = int(input())
    if 0 < x < 100:
        print('Доля вершин в наибольшей компоненте слабой связности:', test_graph.remove_x_perc(x))
    else:
        print('Ошибка ввода')
elif a == 21:
    print('Введите процент узлов наибольшей степени, которые необходимо удалить из графа:')
    x = int(input())
    if 0 < x < 100:
        print('Доля вершин в наибольшей компоненте слабой связности:', test_graph.remove_x_perc_max_degree(x))
    else:
        print('Ошибка ввода')
elif a == 22:
    print('Введите первую вершину:')
    node_1 = input()
    print('Введите вторую вершину:')
    node_2 = input()

    if node_1 not in test_graph.nodes or node_2 not in test_graph.nodes:
        print('Ошибка ввода')
    else:
        print('Введите название нужного алгоритма (basic/sc):')
        alg_name = input()
        print('Введите количество landmarks (5/20/50):')
        landmarks_amount = int(input())
        print('Введите способ выбора landmarks (random/degree/coverage):')
        type_name = input()
        landmarks = []
        if type_name == 'random':
            landmarks = random.sample([n for n in test_graph.nodes], landmarks_amount)
        elif type_name == 'degree':
            landmarks = test_graph.select_landmarks_by_degree(landmarks_amount)
        elif type_name == 'coverage':
            print('Введите число путей для построения landmarks:')
            paths_amount = int(input())
            landmarks = test_graph.select_landmarks_by_coverage(landmarks_amount, paths_amount)
        distances, trees = test_graph.count_distances(landmarks)
        if alg_name == 'basic':
            print(test_graph.landmarks_basic(node_1, node_2, distances))
        elif alg_name == 'sc':
            print(test_graph.landmarks_sc(node_1, node_2, trees))
else:
    print('Ошибка ввода')
