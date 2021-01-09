from DiGraph import DiGraph
from GraphAlgoInterface import GraphAlgoInterface
import json
import heapq


class GraphAlgo(GraphAlgoInterface):
    list = []

    def __init__(self, graph: DiGraph = DiGraph()):
        self.graph = graph
        self.Time = 0

    def get_graph(self):
        return self.graph

    def load_from_json(self, file_name: str):
        with open(file_name) as json_file:
            g = DiGraph()
            x = json.load(json_file)
            for i in x['Nodes']:
               g.add_node(i['id'], i['pos'])
            for j in x['Edges']:
                g.add_edge(j['src'], j['dest'], j['w'])
            self.graph = g
            return True
        return False

    def save_to_json(self, file_name: str):
        data = {}
        data['Nodes'] = []
        data['Edges'] = []
        for i, e in self.graph.get_all_v():
            data['Nodes'].append({'id': i,
                                  'pos': e.pos})
            for x, y in e.neighbors.items():
                data['Edges'].append({'src': i,
                                      'w': y,
                                      'dest': x})
        with open(file_name, 'w') as outfile:
            json.dump(data, outfile)
            return True
        return False

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        if self.graph.get_node(id1) is None or self.graph.get_node(id2) is None:
            return float('inf'), []
        node = self.graph.get_node(id1)
        node.distance = 0
        pq = [(node.distance, node)]
        while len(pq) > 0:
            current_distance, current_node = heapq.heappop(pq)
            if current_node.id == id2:
                break
            if not current_node.visited:
                current_node.visited = True
                for x, k in current_node.neighbors.items():
                    node = self.graph.get_node(x)
                    distance = current_distance + k
                    if node.distance > distance:
                        node.distance = distance
                        node.previous = current_node.id
                        heapq.heappush(pq, (distance, node))
        dist = self.graph.get_node(id2).distance
        if dist == float('inf'):
            self.nullify()
            return dist, []
        temp = id2
        path = []
        while temp != id1:
            path.append(temp)
            temp = self.graph.get_node(temp).previous
        path.append(id1)
        self.nullify()
        path.reverse()
        return dist, path

    def nullify(self):
        for runner in self.graph.get_all_values():
            runner.distance = float('inf')
            runner.previous = None
            runner.visited = False

    def connected_component(self, id1: int):
        stack = []
        node = self.graph.get_node(id1)
        if node is None:
            return self.list
        self.SCC(node, stack)
        l = self.list
        self.nullify_scc()
        return l

    def connected_components(self):
        st = []
        if self.graph.v_size() == 0:
            return self.list
        for temp in self.graph.get_all_values():
            if temp.disc == -1:
                self.SCC(temp, st)

        list_of_list = self.list
        self.nullify_scc()
        return list_of_list

    def plot_graph(self) -> None:
        return

    def SCC(self, u, stack):
        u.disc = self.Time
        u.low = self.Time
        self.Time += 1
        u.visited = True
        stack.append(u)

        for v in u.neighbors.keys():
            vert = self.graph.get_node(v)
            if vert.disc == -1:
                self.SCC(vert, stack)

                u.low = min(u.low, vert.low)
            elif vert.visited is True:
                u.low = min(u.low, vert.disc)

        w = -1  # To store stack extracted vertices
        if u.low == u.disc:
            l2 = []
            while w != u.id:
                node = stack.pop()
                l2.append(node)
                w = node.id
                node.visited = False

            self.list.append(l2)

    def nullify_scc(self):
        self.Time = 0
        self.list = []
        for runner in self.graph.get_all_values():
            runner.visited = False
            runner.disc = -1
            runner.low = -1


if __name__ == '__main__':
    g4 = DiGraph()
    # for i in range(11):
    #     g4.add_node(i)
    # g4.add_edge(0, 1, 0);
    # g4.add_edge(0, 3, 0);
    # g4.add_edge(1, 2, 0);
    # g4.add_edge(1, 4, 0);
    # g4.add_edge(2, 0, 0);
    # g4.add_edge(2, 6, 0);
    # g4.add_edge(3, 2, 0);
    # g4.add_edge(4, 5, 0);
    # g4.add_edge(4, 6, 0);
    # g4.add_edge(5, 6, 0);
    # g4.add_edge(5, 7, 0);
    # g4.add_edge(5, 8, 0);
    # g4.add_edge(5, 9, 0);
    # g4.add_edge(6, 4, 0);
    # g4.add_edge(7, 9, 0);
    # g4.add_edge(8, 9, 0);
    # g4.add_edge(9, 8, 0);
    algo = GraphAlgo(g4)
