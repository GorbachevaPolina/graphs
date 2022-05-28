import networkx as nx
from functions import Graph
import random

print('Введите название файла, в котором находится тестовый граф (с расширением):')
test_file = str(input())

test = nx.read_edgelist(test_file, create_using=nx.Graph(), nodetype=int)
test_graph = Graph(test)

print('Нажмите номер функции, которую необходимо вызвать:')
print('1. Число вершин')
print('2. Число ребер')
print('3. Плотность')
print('4. Число  компонент  слабой связности')
print('5. Количество вершин в наибольшей компоненте слабой связности')
print('6. Число  компонент  сильной связности')
print('7. Количество вершин в наибольшей компоненте сильной связности')
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
    print('Количество вершин в наибольшей компоненте слабой связности: ',
          len(test_graph.weakly_comp_with_max_power()))
elif a == 6:
    di_test = nx.read_edgelist("test.txt", create_using=nx.DiGraph(), nodetype=int)
    di_test_graph = Graph(di_test)
    print('Количество компонент сильной связности: ', di_test_graph.number_strongly_components())
elif a == 7:
    di_test = nx.read_edgelist("test.txt", create_using=nx.DiGraph(), nodetype=int)
    di_test_graph = Graph(di_test)
    print('Количество вершин в наибольшей компоненте сильной связности: ',
          len(test_graph.strongly_comp_with_max_power()))
elif a == 8:
    print('Оценка радиуса наибольшей компоненты слабой связности: ', test_graph.radius())
elif a == 9:
    print('Оценка диаметра наибольшей компоненты слабой связности: ', test_graph.diameter())
elif a == 10:
    print('90 процентиль расстояния наибольшей компоненты слабой связности: ', test_graph.percentile())
elif a == 11:
    di_test = nx.read_edgelist("test.txt", create_using=nx.DiGraph(), nodetype=int)
    di_test_graph = Graph(di_test)
    print('Мета граф: ', di_test_graph.meta_graph())
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
        print('Доля вершин в наибольшей компоненте слабой связности:', test_graph.remove_x_perc(x))
    else:
        print('Ошибка ввода')
elif a == 22:
    print('Введите первую вершину:')
    node_1 = int(input())
    print('Введите вторую вершину:')
    node_2 = int(input())

    if node_1 not in test_graph.nodes or node_2 not in test_graph.nodes:
        print('Ошибка ввода')
    else:
        print('Введите название нужного алгоритма (basic/sc):')
        alg_name = str(input())
        print('Введите количество landmarks (2/5/10):')
        landmarks_amount = int(input())
        print('Введите способ выбора landmarks (random/degree/coverage):')
        type_name = str(input())
        landmarks = []
        if type_name == 'random':
            landmarks = random.sample([n for n in test_graph.nodes()], landmarks_amount)
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
