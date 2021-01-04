from DiGraph import DiGraph
from GraphAlgoInterface import GraphAlgoInterface
import json

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
        return

    def connected_component(self, id1: int) -> list:
        return

    def connected_components(self) -> list[list]:
        return

    def plot_graph(self) -> None:
        return



