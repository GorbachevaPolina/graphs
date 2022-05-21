import networkx as nx
import matplotlib.pyplot as plt


class Graph:
    def __init__(self, graph):
        self.g = graph
        self.nodes = list(nx.nodes(graph))
        self.edges = list(nx.edges(graph))

    def count_nodes(self):
        return len(self.nodes)

    def count_edges(self):
        return len(self.edges)

    def density(self):
        v = self.count_nodes()
        e = self.count_edges()
        return e / ((v*(v-1))/2)

    def neighbors(self, node):
        return list(self.g[node])

    def has_edge(self, u, v):
        return v in list(self.g[u])

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
        plt.plot([row[0] for row in res], [row[1] for row in res], 'bs')
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
        plt.loglog([row[0] for row in res], [row[1] for row in res], 'bs')
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
