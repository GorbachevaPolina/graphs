import networkx as nx
import matplotlib.pyplot as plt
import random


class Graph:
    def __init__(self, graph):
        self.g = nx.to_dict_of_dicts(graph)
        self.nodes = list(nx.nodes(graph))
        self.edges = list(nx.edges(graph))

    def count_nodes(self):
        return len(self.nodes)

    def count_edges(self):
        return len(self.edges)

    def add_edge(self, node1, node2):
        if node1 not in self.nodes:
            self.nodes.append(node1)
        if node2 not in self.nodes:
            self.nodes.append(node2)
        self.edges.append([node1, node2])
        if node1 not in self.g:
            self.g[node1] = {}
        if node2 not in self.g:
            self.g[node2] = {}
        self.g[node1][node2] = {}

    def remove_node(self, node):
        i = 0
        while i < self.count_edges():
            if self.edges[i][0] == node or self.edges[i][1] == node:
                self.edges.remove(self.edges[i])
            else:
                i += 1
        self.nodes.remove(node)
        self.g.pop(node)
        for i in self.g.items():
            if node in i[1]:
                i[1].pop(node)

    def density(self):
        v = self.count_nodes()
        e = self.count_edges()
        return e / ((v*(v-1))/2)

    def neighbors(self, node):
        return list(self.g[node])

    def has_edge(self, u, v):
        return v in self.neighbors(u)

    def degree(self, node):
        neighbors = self.neighbors(node)
        return len(neighbors)

    def local_coef(self, node):
        neighbours = [n for n in self.neighbors(node)]
        len_neighbors = len(neighbours)
        local_coef = 0
        if len_neighbors > 1:
            for node1 in neighbours:
                for node2 in neighbours:
                    if self.has_edge(node1, node2):
                        local_coef += 1
            local_coef /= 2
            local_coef = 2 * local_coef / (len_neighbors * (len_neighbors - 1))
        return [local_coef, len_neighbors]

    def cluster_coef(self):
        res = 0
        for node in self.nodes:
            local_coef, k = self.local_coef(node)
            if k > 1:
                res += local_coef

        return res / len(self.nodes)

    def global_coef(self):
        res = 0
        sum = 0
        for node in self.nodes:
            d = self.degree(node)
            t = (d ** 2 - d) / 2
            res += t * self.local_coef(node)[0]
            sum += t
        return res / sum

    def max_degree(self):
        return max([self.degree(node) for node in self.nodes])

    def min_degree(self):
        return min([self.degree(node) for node in self.nodes])

    def mean_degree(self):
        return sum([self.degree(node) for node in self.nodes]) / len(self.nodes)

    def probability(self):
        arr = [self.degree(node) for node in self.nodes]
        res = [[x, arr.count(x) / len(arr)] for x in set(arr)]
        return res

    def show_probability_function(self):
        res = self.probability()
        plt.plot([row[0] for row in res], [row[1] for row in res])
        plt.show()

    # def show_hist(self):
    #     res = self.probability()
    #     plt.hist([row[0] for row in res],
    #              histtype='step',
    #              cumulative=True,
    #              bins=len([row[0] for row in res]),
    #              weights=[row[1] for row in res])
    #     plt.show()

    def show_log(self):
        res = self.probability()
        plt.loglog([row[0] for row in res], [row[1] for row in res])
        plt.show()

    @staticmethod
    def intersection(n_u, n_v):
        return list(set(n_u) & set(n_v))

    def triangles(self):
        # t = 0
        # for u in self.nodes:
        #     neighbors_u = self.neighbors(u)
        #     for v in neighbors_u:
        #         neighbors_v = self.neighbors(v)
        #         S = self.intersection(neighbors_u, neighbors_v)
        #         t += len(S)
        # return t // 6
        t = 0
        for edge in self.edges:
            if edge[0] != edge[1]:
                neighbors_u = self.neighbors(edge[0])
                neighbors_v = self.neighbors(edge[1])
                S = self.intersection(neighbors_u, neighbors_v)
                # if edge[0] in S:
                #     S.remove(edge[0])
                # if edge[1] in S:
                #     S.remove(edge[1])
                S = [x for x in S if x != edge[0] and x != edge[1]]
                t += len(S)
        return t // 3

    def weak_components(self, func):
        visited = set()
        if func == 'amount':
            amount = 0
        elif func == 'max_comp':
            max_comp = []

        for node in self.nodes:
            if node not in visited:
                visited.add(node)
                nodes_in_check = [node]
                if func == 'amount':
                    amount += 1
                elif func == 'max_comp':
                    curr_comp = [node]
                while nodes_in_check:
                    v = nodes_in_check.pop(0)
                    for neighbour in self.neighbors(v):
                        if neighbour not in visited:
                            visited.add(neighbour)
                            nodes_in_check.append(neighbour)
                            if func == 'max_comp':
                                curr_comp.append(neighbour)
                if func == 'max_comp' and len(curr_comp) > len(max_comp):
                    max_comp = curr_comp
        if func == 'amount':
            return amount
        elif func == 'max_comp':
            return max_comp

    def number_weakly_components(self):
        return self.weak_components('amount')

    def weakly_comp_with_max_power(self):
        return self.weak_components('max_comp')

    def fill_order(self, node, visited, order):
        visited.add(node)
        for neighbour in self.neighbors(node):
            if neighbour not in visited:
                self.fill_order(neighbour, visited, order)
        order.append(node)

    def dfs(self, node, visited, curr_comp):
        visited.add(node)
        curr_comp.append(node)
        for neighbour in self.neighbors(node):
            if neighbour not in visited:
                self.dfs(neighbour, visited, curr_comp)

    def transpose(self):
        transp = Graph(nx.DiGraph())
        for edge in self.edges:
            transp.add_edge(edge[1], edge[0])
        return transp

    def strong_components(self, func):
        order = []
        visited = set()
        if func == 'max_comp':
            max_comp = []
        for node in self.nodes:
            if node not in visited:
                self.fill_order(node, visited, order)

        transposed_graph = self.transpose()

        if func == 'amount':
            amount = 0
        elif func == 'meta':
            roots_nodes = dict()
            roots = []
        visited = set()
        while order:
            node = order.pop()
            curr_comp = []
            if node not in visited:
                transposed_graph.dfs(node, visited, curr_comp)
                if func == 'amount':
                    amount += 1
                elif func == 'max_comp' and len(curr_comp) > len(max_comp):
                    max_comp = curr_comp
                elif func == 'meta':
                    root = curr_comp.pop()
                    roots.append(root)
                    roots_nodes[root] = root
                    for v in curr_comp:
                        roots_nodes[v] = root
        if func == 'amount':
            return amount
        elif func == 'max_comp':
            return max_comp
        elif func == 'meta':
            meta = nx.DiGraph()
            meta.add_nodes_from(roots)
            for edge in self.edges:
                first_root = roots_nodes[edge[0]]
                second_root = roots_nodes[edge[1]]
                if first_root != second_root:
                    meta.add_edge(first_root, second_root)
            return meta

    def number_strongly_components(self):
        return self.strong_components('amount')

    def strongly_comp_with_max_power(self):
        return self.strong_components('max_comp')

    def meta_graph(self):
        return self.strong_components('meta')

    def distances(self, amount=500):
        component = self.weakly_comp_with_max_power()
        if len(component) > amount:
            sample = random.sample(component, amount)
        else:
            sample = component

        n = len(component)
        eccentricity = set()
        distances_for_perc = set()

        for node in sample:
            distance = dict()
            nodes_in_check = []
            visited = set()
            dst_sample = set()

            distance[node] = 0
            visited.add(node)
            nodes_in_check.append(node)

            while nodes_in_check:
                v = nodes_in_check.pop(0)
                for neighbour in self.neighbors(v):
                    if neighbour not in visited:
                        visited.add(neighbour)
                        nodes_in_check.append(neighbour)
                        distance[neighbour] = distance[v] + 1
                        if neighbour in sample:
                            dst_sample.add(distance[neighbour])
                            distances_for_perc.add(distance[neighbour])
            max_dist = 0
            for dist in dst_sample:
                max_dist = max(max_dist, dist)
            eccentricity.add(max_dist)
        return [eccentricity, distances_for_perc]

    def radius(self):
        eccentricity = list(self.distances()[0])
        radius = eccentricity[0]
        for i in range(len(eccentricity)):
            radius = min(radius, eccentricity[i])
        return radius

    def diameter(self):
        eccentricity = list(self.distances()[0])
        d = eccentricity[0]
        for i in range(len(eccentricity)):
            d = max(d, eccentricity[i])
        return d

    def percentile(self, percent=90):
        distances = sorted(list(self.distances()[1]))
        perc = distances[int(len(distances) * percent / 100)]
        return perc

    def remove_x_perc(self, x):
        amount = int(self.count_nodes() * x / 100)
        remove_nodes = random.sample(self.nodes, amount)
        for node in remove_nodes:
            self.remove_node(node)
        return len(self.weakly_comp_with_max_power())

    def degree_quicksort(self, del_nodes, degree):
        if len(del_nodes) <= 1:
            return del_nodes
        else:
            q = random.choice(del_nodes)

        left, middle, right = (list() for _ in range(3))
        for n in del_nodes:
            if degree[n] > degree[q]:
                left.append(n)
            if degree[n] < degree[q]:
                right.append(n)
            if degree[n] == degree[q]:
                middle.append(n)
        return self.degree_quicksort(left, degree) + middle + self.degree_quicksort(right, degree)

    def remove_x_perc_max_degree(self, x):
        amount = int(self.count_nodes() * x / 100)
        del_nodes = [node for node in self.nodes]
        degree = dict()
        for node in self.nodes:
            degree[node] = self.degree(node)
        del_nodes = self.degree_quicksort(del_nodes, degree)
        for i in range(amount):
            self.remove_node(del_nodes[i])
        return len(self.weakly_comp_with_max_power())
