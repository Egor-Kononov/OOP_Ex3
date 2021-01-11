import random
from collections import deque
from datetime import datetime
from DiGraph import DiGraph
from GraphAlgoInterface import GraphAlgoInterface
import json
import heapq
import matplotlib.pyplot as plt


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, graph: DiGraph = DiGraph()):
        self.graph = graph
        self.list = []

    def get_graph(self):
        return self.graph
     
    def load_from_json(self, file_name: str):
        with open(file_name) as json_file:
            g = DiGraph()
            x = json.load(json_file)
            for i in x['Nodes']:
                if 'pos' in i.keys():
                    if type(i['pos']) == str:
                        temp = []
                        for s in i['pos'].split(","):
                            temp.append(float(s))
                        tup = (temp[0], temp[1], temp[2])
                        g.add_node(i['id'], tup)
                    else:
                        g.add_node(i['id'], i['pos'])
                else:
                    g.add_node(i['id'])
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
                                  'pos': f"{str(e.pos[0])},{str(e.pos[1])},{str(e.pos[2])}"})
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
        if id1 == id2:
            return 0, [id1]
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
        node = self.graph.get_node(id1)
        if node is None:
            return self.list
        gr = self.transpose()
        self.scc(node, gr)
        for list1 in self.list:
            if node in list1:
                self.nullify_scc()
                return list1
        return list

    def connected_components(self):
        if self.graph.v_size() == 0:
            return self.list
        gr = self.transpose()
        for temp in self.graph.get_all_values():
            if temp.disc == -1:
                self.scc(temp, gr)
        list_of_list = self.list
        self.nullify_scc()
        return list_of_list

    def plot_graph(self) -> None:
        if self.graph is None:
            return
        x1 = []
        y1 = []
        for key in self.graph.graph.keys():
            pos = self.graph.graph[key].pos
            if pos == (0, 0, 0):
                self.graph.graph[key].pos = (random.uniform(0.0, 70), random.uniform(0.0, 70), 0.0)
                pos = self.graph.graph[key].pos
            else:

                pos = (pos[0], pos[1], pos[2])
            self.graph.graph[key].pos = pos
            x1.append(pos[0])
            y1.append(pos[1])
        plt.plot(x1, y1, '.', color='blue')
        for key in self.graph.graph.keys():
            plt.annotate(key, xy=(self.graph.graph[key].pos[0], self.graph.graph[key].pos[1]), xycoords='data',
                         bbox=dict(boxstyle="round4,pad=.5", fc="0.9"),
                         xytext=(self.graph.graph[key].pos[0], self.graph.graph[key].pos[1]), textcoords='data',
                         arrowprops=dict(arrowstyle="<|-|>"))
            for kei in self.graph.graph[key].neighbors.keys():
                plt.annotate(key, xy=(self.graph.graph[kei].pos[0], self.graph.graph[kei].pos[1]), xycoords='data',
                             bbox=dict(boxstyle="round4,pad=.5", fc="0.9"),
                             xytext=(self.graph.graph[key].pos[0], self.graph.graph[key].pos[1]), textcoords='data',
                             arrowprops=dict(arrowstyle="-|>"))

        plt.title("Graph")
        plt.show()

    def bfs(self, node, gr):
        stack = deque()
        if node.visited:
            pass
        else:
            queue = deque()
            queue.append(node)
            while len(queue) != 0:
                temp = queue.popleft()
                if temp.visited:
                    pass
                else:
                    stack.append(temp.id)
                    temp.visited = True
                    for i in temp.neighbors.keys():
                        var = gr.get_node(i)
                        if var.visited:
                            pass
                        else:
                            queue.append(var)
        return stack

    def bfs1(self, node, gr, st):
        stack = deque()
        if node.visited:
            pass
        else:
            queue = deque()
            queue.append(node)
            while len(queue) != 0:
                temp = queue.popleft()
                if temp.visited:
                    pass
                else:
                    stack.append(temp)
                    temp.visited = True
                    for i in temp.neighbors.keys():
                        var = gr.get_node(i)
                        if var.visited or i not in st:
                            pass
                        else:
                            queue.append(var)
        return stack

    def scc(self, node, gr):
        stack = self.bfs(node, self.graph)
        while len(stack) != 0:
            temp = self.graph.get_node(stack.popleft())
            if temp.low == -1:
                con_st = self.bfs1(gr.get_node(temp.id), gr, stack)
                con_list = []
                while len(con_st) != 0:
                    temp = con_st.popleft()
                    node = self.graph.get_node(temp.id)
                    node.disc = 0
                    node.low = 0
                    con_list.append(node)
                self.list.append(con_list)

    def transpose(self):
        g = DiGraph()
        for i in self.graph.get_all_values():
            g.add_node(i.id, i.pos)
        for node in self.graph.get_all_values():
            for dst, w in node.neighbors.items():
                g.add_edge(dst, node.id, w)
        return g
     
    def nullify_scc(self):
        self.list = []
        for runner in self.graph.get_all_values():
            runner.visited = False
            runner.disc = -1
            runner.low = -1
