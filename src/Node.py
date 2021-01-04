class Node:

    def __init__(self, id: int = 0, pos: tuple = None):
        self.id = id
        self.pos = pos
        self.neighbors = dict()

    def __str__(self) -> str:
        return f"str : Node id:{self.id}, pos:{self.pos}, Neighbors:{self.neighbors}"

    def __repr__(self):
        return f"repr : Node id:{self.id}, pos:{self.pos}, Neighbors:{self.neighbors}"

    def add_edge(self, dest: int, weight: float):
        self.neighbors[dest] = weight
