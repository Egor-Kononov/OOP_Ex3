
from src.GraphInterface import GraphInterface


class DiGraph(GraphInterface):

    def __init__(self):
        self.graph = {}
        self.edge_size = 0
        self.mc = 0

    def __repr__(self):
        return f"graph :  e_size:{self.edge_size}, v_size:{len(self.graph)}, mc:{self.mc}"

    def v_size(self):
        return len(self.graph)

    def e_size(self):
        return self.edge_size

    def get_all_v(self):
        return self.graph.items()

    def all_in_edges_of_node(self, id1: int):
        edges_dict = {}
        for i in self.graph.values():
            if id1 in i.neighbors:
                edges_dict[i.id] = i.neighbors[id1]
        return edges_dict.items()

    def all_out_edges_of_node(self, id1: int):
        return self.graph[id1].neighbors.items()

    def add_node(self, node_id: int, pos: tuple = None):
        if node_id in self.graph:
            return False

        node = Node(node_id, pos)
        self.graph[node.id] = node
        self.mc += 1
        return True

    def remove_node(self, node_id: int):
        if node_id in self.graph:
            for i in self.graph.values():
                if node_id in i.neighbors:
                    i.remove_neighbor(node_id)
                    self.edge_size -= 1
            self.edge_size -= len(self.graph[node_id].neighbors)
            self.graph.pop(node_id)
            self.mc += 1
            return True
        return False

    def get_mc(self):
        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float):
        if id1 not in self.graph or id2 not in self.graph or id2 in self.graph[id1].neighbors or weight < 0:
            return False
        self.graph[id1].add_neighbor(id2, weight)
        self.edge_size += 1
        self.mc += 1
        return True

    def remove_edge(self, node_id1: int, node_id2: int):
        if node_id1 not in self.graph or node_id2 not in self.graph or node_id2 not in self.graph[node_id1].neighbors:
            return False
        self.graph[node_id1].remove_neighbor(node_id2)
        self.edge_size -= 1
        self.mc += 1
        return True


class Node:

    def __init__(self, id: int = 0, pos: tuple = None):
        self.id = id
        self.pos = pos
        self.neighbors = dict()

    def __repr__(self):
        return f"node : node_id:{self.id}, pos:{self.pos}, Neighbors:{self.neighbors}"

    def add_neighbor(self, dest: int, weight: float):
        self.neighbors[dest] = weight

    def remove_neighbor(self, dest: int):
        self.neighbors.pop(dest)


