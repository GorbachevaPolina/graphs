import networkx as nx
import matplotlib.pyplot as plt
import random


class Graph:
    def __init__(self, graph):
        # self.g = graph
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

    def remove_node(self, node):
        i = 0
        while i < self.count_edges():
            if self.edges[i][0] == node or self.edges[i][1] == node:
                self.edges.remove(self.edges[i])
            else:
                i += 1
        self.nodes.remove(node)

    def density(self):
        v = self.count_nodes()
        e = self.count_edges()
        return e / ((v*(v-1))/2)

    def neighbors(self, node):
        # return list(self.g[node])
        n = []
        for edge in self.edges:
            if edge[0] == node:
                n.append(edge[1])
            elif edge[1] == node:
                n.append(edge[0])
        return n

    def di_neighbors(self, node):
        # return list(self.g[node])
        n = []
        for edge in self.edges:
            if edge[0] == node:
                n.append(edge[1])
        return n

    def has_edge(self, u, v):
        # return v in list(self.g[u])
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

    def show_hist(self):
        res = self.probability()
        plt.hist([row[0] for row in res],
                 histtype='step',
                 cumulative=True,
                 bins=len([row[0] for row in res]),
                 weights=[row[1] for row in res])
        plt.show()

    def show_log(self):
        res = self.probability()
        plt.loglog([row[0] for row in res], [row[1] for row in res])
        plt.show()

    @staticmethod
    def intersection(n_u, n_v):
        return list(set(n_u) & set(n_v))

    def triangles(self):
        t = 0
        for u in self.nodes:
            neighbors_u = self.neighbors(u)
            for v in neighbors_u:
                neighbors_v = self.neighbors(v)
                S = self.intersection(neighbors_u, neighbors_v)
                t += len(S)
        return t // 6

    def weak_components(self):
        visited = set()
        amount = 0

        for node in self.nodes:
            if node not in visited:
                amount += 1
                visited.add(node)
                comp = [node]
                while comp:
                    v = comp.pop()
                    for neighbour in self.neighbors(v):
                        if neighbour not in visited:
                            visited.add(neighbour)
                            comp.append(neighbour)
        return amount

    def max_weakly_comp(self):
        visited = set()
        max_comp = []

        for node in self.nodes:
            if node not in visited:
                visited.add(node)
                curr_comp = [node]
                nodes_in_check = [node]

                while nodes_in_check:
                    v = nodes_in_check.pop()
                    for neighbour in self.neighbors(v):
                        if neighbour not in visited:
                            visited.add(neighbour)
                            nodes_in_check.append(neighbour)
                            curr_comp.append(neighbour)

                if len(curr_comp) > len(max_comp):
                    max_comp = curr_comp
        return max_comp

    def weakly_comp_with_max_power(self):
        return len(self.max_weakly_comp()) / self.count_nodes()

    def fill_order(self, node, visited, order):
        visited.add(node)
        for neighbour in self.di_neighbors(node):
            if neighbour not in visited:
                self.fill_order(neighbour, visited, order)
        order.append(node)

    def dfs(self, node, visited, curr_comp):
        visited.add(node)
        curr_comp.append(node)
        for neighbour in self.di_neighbors(node):
            if neighbour not in visited:
                self.dfs(neighbour, visited, curr_comp)

    def transpose(self):
        transp = Graph(nx.DiGraph())
        for edge in self.edges:
            transp.add_edge(edge[1], edge[0])
        return transp

    def strong_components(self):
        order = []
        visited = set()
        for node in self.nodes:
            if node not in visited:
                self.fill_order(node, visited, order)

        transposed_graph = self.transpose()
        visited = set()
        amount = 0
        while order:
            node = order.pop()
            if node not in visited:
                transposed_graph.dfs(node, visited, [])
                amount += 1
        return amount

    def strongly_comp_with_max_power(self):
        max_comp = []
        order = []
        visited = set()
        for node in self.nodes:
            if node not in visited:
                self.fill_order(node, visited, order)

        transposed_graph = self.transpose()
        visited = set()
        while order:
            node = order.pop()
            curr_comp = []
            if node not in visited:
                transposed_graph.dfs(node, visited, curr_comp)
                if len(curr_comp) > len(max_comp):
                    max_comp = curr_comp

        return len(max_comp) / self.count_nodes()

    def meta_graph(self):
        order = []
        visited = set()
        for node in self.nodes:
            if node not in visited:
                self.fill_order(node, visited, order)

        transposed_graph = self.transpose()

        roots_nodes = dict()
        roots = []

        visited = set()
        while order:
            node = order.pop()
            comp = []
            if node not in visited:
                transposed_graph.dfs(node, visited, comp)

                root = comp.pop()
                roots.append(root)
                roots_nodes[root] = root
                for v in comp:
                    roots_nodes[v] = root

        meta = nx.DiGraph()
        meta.add_nodes_from(roots)
        for edge in self.edges:
            first_root = roots_nodes[edge[0]]
            second_root = roots_nodes[edge[1]]
            if first_root != second_root:
                meta.add_edge(first_root, second_root)
        nx.draw_networkx(meta)
        plt.show()

    def distances_500(self):
        component = self.max_weakly_comp()
        if len(component) > 500:
            sample = random.sample(component, 500)
        else:
            sample = component

        n = len(sample)
        distances = [[-1] * n for i in range(n)]

        for node in sample:
            nodes_in_check = []
            index = sample.index(node)
            visited = set()
            dst_all = dict()
            count_visit = n - 1 - index

            distances[index][index] = 0
            dst_all[node] = 0
            visited.add(node)
            nodes_in_check.append(node)

            while nodes_in_check and count_visit > 0:
                v = nodes_in_check.pop()
                for neighbour in self.neighbors(v):
                    if neighbour not in visited:
                        visited.add(neighbour)
                        nodes_in_check.append(neighbour)
                        # neigh_ind = self.nodes.index(neighbour)
                        dst_all[neighbour] = dst_all[v] + 1
                        if neighbour in sample and index < sample.index(neighbour):
                            distances[index][sample.index(neighbour)] = dst_all[neighbour]
                            distances[sample.index(neighbour)][index] = dst_all[neighbour]
                            count_visit -= 1

        n = len(distances[0])
        eccentricity = [-1] * n
        for i in range(n):
            for j in range(n):
                eccentricity[i] = max(eccentricity[i], distances[i][j])
        radius = eccentricity[0]
        d = eccentricity[0]
        for i in range(len(eccentricity)):
            radius = min(radius, eccentricity[i])
            d = max(d, eccentricity[i])
        print('оценка радиуса: ', radius)
        print('оценка диаметра: ', d)

        dsts = []
        for i in range(len(distances[0])):
            for j in range(i + 1, len(distances[0])):
                dsts.append(distances[i][j])
        dsts.sort()
        perc = dsts[int(len(dsts) * 0.9)]
        print('90 процентиль:', perc)

        return distances

    def eccentricity(self, distances):
        n = len(distances[0])
        eccentricity = [-1] * n
        for i in range(n):
            for j in range(n):
                eccentricity[i] = max(eccentricity[i], distances[i][j])
        return eccentricity

    def radius(self):
        eccentricity = self.eccentricity(self.distances_500())
        radius = eccentricity[0]
        for i in range(len(eccentricity)):
            radius = min(radius, eccentricity[i])
        return radius

    def diameter(self):
        eccentricity = self.eccentricity(self.distances_500())
        d = eccentricity[0]
        for i in range(len(eccentricity)):
            d = max(d, eccentricity[i])
        return d
    
    def percentile_90(self):
        distances = self.distances_500()

        dsts = []
        for i in range(len(distances[0])):
            for j in range(i + 1, len(distances[0])):
                dsts.append(distances[i][j])
        dsts.sort()
        perc = dsts[int(len(dsts) * 0.9)]
        return perc

    def remove_x_perc(self, x):
        amount = int(self.count_nodes() * x / 100)
        remove_nodes = random.sample(self.nodes, amount)
        for node in remove_nodes:
            self.remove_node(node)
            print(node)
        return self.weakly_comp_with_max_power()
        # nx.remove_nodes_from(self.g, remove_nodes)
        # return max(nx.connected_components(self.g), key=len) / nx.number_of_nodes(self.g)

    def remove_x_perc_max_degree(self, x):
        amount = int(self.count_nodes() * x / 100)
        degrees = dict()
        for node in self.nodes:
            degrees[node] = self.degree(node)
        degrees.sort(key=lambda a: a[1], reverse=True)
        i = 0
        while amount > i:
            curr_node = degrees[i][0]
            self.remove_node(curr_node)
            i += 1
        return self.weakly_comp_with_max_power()
