import matplotlib.pyplot as plt
import random


def quicksort(nodes, degree):
    if len(nodes) <= 1:
        return nodes
    else:
        q = random.choice(nodes)

    left, middle, right = (list() for _ in range(3))
    for n in nodes:
        if degree[n] > degree[q]:
            left.append(n)
        if degree[n] < degree[q]:
            right.append(n)
        if degree[n] == degree[q]:
            middle.append(n)

    return quicksort(left, degree) + middle + quicksort(right, degree)


class DiGraph:
    def __init__(self, n=None, e=None):
        if n is None:
            self.nodes = set()
        else:
            self.nodes = set(n)

        if e is None:
            self.edges = dict()
        else:
            self.edges = dict([(v, set()) for v in self.nodes])
            for i in e:
                self.add_edge(i[0], i[1])

    def count_nodes(self):
        return len(self.nodes)

    def count_edges(self):
        return sum([self.degree(node) for node in self.nodes])

    def neighbors(self, node):
        return self.edges[node]

    def degree(self, node):
        neighbors = self.neighbors(node)
        res = len(neighbors)
        return res

    def add_edge(self, u, v):
        if u not in self.nodes:
            self.nodes.add(u)
            self.edges[u] = set()
        if v not in self.nodes:
            self.nodes.add(v)
            self.edges[v] = set()
        if v not in self.edges[u]:
            self.edges[u].add(v)

    def edges_list(self):
        edges = set()
        for v in self.edges.keys():
            for u in self.edges[v]:
                edges.add((v, u))
        return edges

    def strong_components(self):
        indexes = dict()
        links = dict()
        visited = set()
        done = set()
        stack_component = []
        components = dict()
        counter = 0
        comp_counter = 0

        for node in self.nodes:
            if node not in done:
                stack_nodes = [node]

                while stack_nodes:
                    s = stack_nodes[-1]
                    unvisited_node = None

                    if s not in visited:
                        counter += 1
                        indexes[s] = counter
                        links[s] = counter
                        visited.add(s)

                    for t in self.neighbors(s):
                        if t not in visited:
                            unvisited_node = t
                            stack_nodes.append(t)
                            break

                    if not unvisited_node:
                        stack_nodes.pop()

                        for v in self.neighbors(s):
                            if v not in done:
                                links[s] = min([links[s], links[v]])

                        stack_component.append(s)

                        if links[s] == indexes[s]:
                            comp_counter += 1

                            while stack_component:
                                node = stack_component.pop()

                                if indexes[node] < indexes[s]:
                                    stack_component.append(node)
                                    break
                                else:
                                    if comp_counter not in components.keys():
                                        components[comp_counter] = {node}
                                    else:
                                        components[comp_counter].add(node)
                                    done.add(node)

        return components

    def number_strongly_components(self):
        return len(self.strong_components().keys())

    def strongly_comp_with_max_power(self):
        max_len = 0
        max_comp = -1
        components = self.strong_components()
        for i in components.keys():
            if len(components[i]) > max_len:
                max_len = len(components[i])
                max_comp = i
        return components[max_comp]

    def nodes_in_strongly_comp_with_max_power(self):
        return len(self.strongly_comp_with_max_power()) / self.count_nodes()

    def meta_graph(self):
        scc = self.strong_components()
        new_nodes = set(scc.keys())
        new_edges = set()
        indexes = dict()
        for node, values in scc.items():
            for value in values:
                indexes[value] = node
        for edge in self.edges_list():
            u = indexes[edge[0]]
            v = indexes[edge[1]]
            if u != v:
                new_edges.add((u, v))
        meta = DiGraph(new_nodes, new_edges)
        return meta


class Graph:
    def __init__(self, n=None, e=None):
        if n is None:
            self.nodes = set()
        else:
            self.nodes = set(n)

        if e is None:
            self.edges = dict()
        else:
            self.edges = dict([(v, set()) for v in self.nodes])
            for i in e:
                self.add_edge(i[0], i[1])

    def count_nodes(self):
        return len(self.nodes)

    def count_edges(self):
        return sum([self.degree(node) for node in self.nodes]) // 2

    def edges_list(self):
        edges = set()
        for v in self.edges.keys():
            for u in self.edges[v]:
                if (u, v) not in edges:
                    edges.add((v, u))
        return edges

    def add_edge(self, u, v):
        if u not in self.nodes:
            self.nodes.add(u)
            self.edges[u] = set()
        if v not in self.nodes:
            self.nodes.add(v)
            self.edges[v] = set()
        if v not in self.edges[u]:
            self.edges[u].add(v)
            self.edges[v].add(u)

    def remove_node(self, node):
        self.nodes.remove(node)
        self.edges.pop(node)
        for item in self.edges.items():
            if node in item[1]:
                item[1].remove(node)

    def density(self):
        v = self.count_nodes()
        e = self.count_edges()
        return e / ((v*(v-1))/2)

    def neighbors(self, node):
        return self.edges[node]

    def has_edge(self, u, v):
        return v in self.neighbors(u)

    def degree(self, node):
        neighbors = self.neighbors(node)
        res = len(neighbors)
        if node in neighbors:
            res += 1
        return res

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

    def show_log(self):
        res = self.probability()
        plt.loglog([row[0] for row in res], [row[1] for row in res], 'bs')
        plt.show()

    @staticmethod
    def intersection(n_u, n_v):
        return list(set(n_u) & set(n_v))

    def triangles(self):
        t = 0
        for edge in self.edges_list():
            if edge[0] != edge[1]:
                neighbors_u = self.neighbors(edge[0])
                neighbors_v = self.neighbors(edge[1])
                S = self.intersection(neighbors_u, neighbors_v)
                S = [x for x in S if x != edge[0] and x != edge[1]]
                t += len(S)
        return t // 3

    def weak_components(self):
        visited = set()
        counter = 0
        components = dict()

        for node in self.nodes:
            if node not in visited:
                visited.add(node)
                nodes_in_check = [node]
                counter += 1
                components[counter] = {node}

                while nodes_in_check:
                    v = nodes_in_check.pop(0)
                    for neighbour in self.neighbors(v):
                        if neighbour not in visited:
                            visited.add(neighbour)
                            nodes_in_check.append(neighbour)
                            components[counter].add(neighbour)
        return components

    def number_weakly_components(self):
        return len(self.weak_components().keys())

    def weakly_comp_with_max_power(self):
        max_len = 0
        max_comp = -1
        components = self.weak_components()
        for i in components.keys():
            if len(components[i]) > max_len:
                max_len = len(components[i])
                max_comp = i
        return components[max_comp]

    def nodes_in_weakly_comp_with_max_power(self):
        return len(self.weakly_comp_with_max_power()) / self.count_nodes()

    def distances(self, amount=500):
        component = self.weakly_comp_with_max_power()
        if len(component) > amount:
            sample = random.sample(component, amount)
        else:
            sample = component

        eccentricity = set()
        distances = []

        for node in sample:
            distance = dict()
            nodes_in_check = [node]
            visited = {node}

            distance[node] = 0
            max_dist = 0
            while nodes_in_check:
                v = nodes_in_check.pop(0)
                for neighbour in self.neighbors(v):
                    if neighbour not in visited:
                        visited.add(neighbour)
                        nodes_in_check.append(neighbour)
                        distance[neighbour] = distance[v] + 1
                        if neighbour in sample:
                            max_dist = max(max_dist, distance[neighbour])
                            distances.append(distance[neighbour])
            eccentricity.add(max_dist)
        return [eccentricity, distances]

    def radius(self):
        eccentricity = list(self.distances()[0])
        return min(eccentricity)

    def diameter(self):
        eccentricity = list(self.distances()[0])
        return max(eccentricity)

    def percentile(self, percent=90):
        distances = sorted(list(self.distances()[1]))
        perc = distances[int(len(distances) * percent / 100)]
        return perc

    def remove_x_perc(self, x):
        amount = int(self.count_nodes() * x / 100)
        remove_nodes = random.sample(self.nodes, amount)
        for node in remove_nodes:
            self.remove_node(node)
        return self.nodes_in_weakly_comp_with_max_power() / self.count_nodes()

    def remove_x_perc_max_degree(self, x):
        amount = int(self.count_nodes() * x / 100)
        degree = dict()
        for node in self.nodes:
            degree[node] = self.degree(node)
        del_nodes = quicksort(list(self.nodes), degree)
        for i in range(amount):
            self.remove_node(del_nodes[i])
        return self.nodes_in_weakly_comp_with_max_power() / self.count_nodes()

    def select_landmarks_by_degree(self, amount):
        degree = dict()
        for node in self.nodes:
            degree[node] = self.degree(node)

        return quicksort(list(self.nodes), degree)[:amount]

    def bfs(self, node):
        distance = dict()
        tree = dict()
        queue = []
        visited = set()
        distance[node] = 0
        visited.add(node)
        queue.append(node)

        while queue:
            s = queue.pop(0)

            for neighbour in self.neighbors(s):
                if neighbour not in visited:
                    distance[neighbour] = distance[s] + 1
                    tree[neighbour] = s
                    visited.add(neighbour)
                    queue.append(neighbour)

        return distance, tree

    def count_distances(self, landmarks):
        distances = dict()
        trees = dict()

        for landmark in landmarks:
            distances[landmark], trees[landmark] = self.bfs(landmark)

        return distances, trees

    @staticmethod
    def landmarks_basic(s, t, distances):
        distance = 1e9

        for landmark in distances.keys():
            list = distances[landmark]

            if s in list and t in list:
                current_distance = list[s] + list[t]
                if current_distance < distance:
                    distance = current_distance

        return distance

    @staticmethod
    def find_path(node, tree):
        path = []

        while True:
            path.append(node)
            if node in tree:
                node = tree[node]
            else: break

        return path

    def landmarks_sc(self, s, t, trees):
        distance = 1e9

        for landmark in trees.keys():
            tree = trees[landmark]
            path_to_s = self.find_path(s, tree)
            path_to_t = self.find_path(t, tree)

            if len(path_to_s) == 1 or len(path_to_t) == 1: continue
            path_to_s.pop(); path_to_t.pop()

            path_len = len(path_to_s) + len(path_to_t)
            if path_len < distance:
                distance = path_len

            for v in path_to_s:
                for w in path_to_t:
                    v_index = path_to_s.index(v)
                    w_index = path_to_t.index(w)

                    if self.has_edge(v, w) and v_index + w_index + 1 < distance:
                        distance = v_index + w_index + 1

        return distance

    def bfs_for_pair(self, node, target):
        tree = dict()
        queue = []
        visited = set()
        visited.add(node)
        queue.append(node)

        while queue:
            s = queue.pop(0)

            for neighbour in self.neighbors(s):
                if neighbour not in visited:
                    tree[neighbour] = s
                    visited.add(neighbour)
                    queue.append(neighbour)

                    if neighbour == target:
                        queue = []
                        break

        return tree

    def select_landmarks_by_coverage(self, amount, pairs_amount):
        pairs = set()
        paths = dict([(v, set()) for v in range(pairs_amount)])
        landmarks = []

        for i in range(pairs_amount):
            while True:
                [node_1, node_2] = random.sample(self.nodes, 2)
                hash1 = str(node_1) + '_' + str(node_2)
                hash2 = str(node_2) + '_' + str(node_1)

                if hash1 not in pairs and hash2 not in pairs and node_1 != node_2:
                    pairs.add(hash1)

                    tree = self.bfs_for_pair(node_1, node_2)
                    path = set(self.find_path(node_2, tree))

                    if len(path) == 1: continue
                    paths[i] = path
                    break

        while amount > 0:
            vertex_count = dict()

            for path in paths.values():
                for node in path:
                    if node not in vertex_count.keys():
                        vertex_count[node] = 0
                    else:
                        vertex_count[node] += 1

            max_coverage = -1; max_node = -1
            for n in vertex_count.keys():
                current_coverage = vertex_count[n]
                if current_coverage > max_coverage:
                    max_coverage = current_coverage
                    max_node = n

            new_paths = dict()
            for n in paths.keys():
                if max_node not in paths[n]:
                    new_paths[n] = paths[n]
            paths = new_paths

            if max_node == -1: break
            landmarks.append(max_node)
            amount -= 1

        return landmarks
