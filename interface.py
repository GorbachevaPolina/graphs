import networkx as nx
from functions import Graph

test = nx.read_edgelist("test.txt", create_using=nx.Graph(), nodetype=int)
test_graph = Graph(test)

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
a = int(input())
if a == 1:
    print('Количество вершин: ', test_graph.count_nodes())
elif a == 2:
    print('Количество ребер: ', test_graph.count_edges())
elif a == 3:
    print('Плотность: ', test_graph.density())
elif a == 4:
    print('Количество компонент слабой связности: ', test_graph.weak_components())
elif a == 5:
    print('Доля вершин в наибольшей компоненте слабой связности: ', test_graph.weakly_comp_with_max_power())
elif a == 6:
    di_test = nx.read_edgelist("test.txt", create_using=nx.DiGraph(), nodetype=int)
    di_test_graph = Graph(di_test)
    print('Количество компонент сильной связности: ', di_test_graph.strong_components())
elif a == 7:
    di_test = nx.read_edgelist("test.txt", create_using=nx.DiGraph(), nodetype=int)
    di_test_graph = Graph(di_test)
    print('Доля вершин в наибольшей компоненте слабой связности: ', test_graph.weakly_comp_with_max_power())
elif a == 8:
    print('Оценка радиуса наибольшей компоненты слабой связности: ', test_graph.radius())
elif a == 9:
    print('Оценка диаметра наибольшей компоненты слабой связности: ', test_graph.diameter())
elif a == 10:
    print('90 процентиль расстояния наибольшей компоненты слабой связности: ', test_graph.percentile_90())
elif a == 11:
    di_test = nx.read_edgelist("test.txt", create_using=nx.DiGraph(), nodetype=int)
    di_test_graph = Graph(di_test)
    di_test_graph.meta_graph()
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
    test_graph.show_hist()
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
else:
    print('Ошибка ввода')
