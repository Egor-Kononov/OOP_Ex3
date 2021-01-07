from DiGraph import DiGraph
from GraphAlgoInterface import GraphAlgoInterface
import json
import heapq


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, graph: DiGraph = DiGraph()):
        self.graph = graph

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

    def connected_component(self, id1: int) -> list:
        return

    def connected_components(self) -> list[list]:
        return

    def plot_graph(self) -> None:
        return


if __name__ == '__main__':
    g = DiGraph()
    for i in range(6):
        g.add_node(i)
    g.add_edge(0, 1, 2)
    g.add_edge(1, 2, 5)
    g.add_edge(1, 4, 10)
    g.add_edge(2, 3, 1)
    g.add_edge(3, 4, 1)
    algo = GraphAlgo(g)
    algo.load_from_json("A0")
    print(algo.get_graph())