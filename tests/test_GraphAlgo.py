import unittest

from DiGraph import DiGraph
from GraphAlgo import GraphAlgo


class MyTest(unittest.TestCase):

    def setUp(self) -> None:
        gr = DiGraph()
        for i in range(9):
            gr.add_node(i)
        gr.add_edge(0, 1, 5)
        gr.add_edge(1, 2, 3)
        gr.add_edge(1, 4, 17.5)
        gr.add_edge(2, 3, 10)
        gr.add_edge(2, 4, 6.5)
        gr.add_edge(3, 4, 5)
        gr.add_edge(4, 1, 17.5)
        gr.add_edge(3, 5, 7)
        gr.add_edge(5, 6, 5)
        gr.add_edge(6, 5, 5)
        gr.add_edge(7, 6, 2)
        self.algo = GraphAlgo(gr)

    def test_Save_and_load(self):
        file_name = "graph.json"
        self.algo.save_to_json(file_name)
        al = GraphAlgo()
        al.load_from_json("graph.json")
        self.assertEqual(self.algo.graph, al.graph)

    def test_short_path(self):
        self.assertTrue(self.algo.shortest_path(0, 4) == (14.5, [0, 1, 2, 4]))
        self.assertTrue(self.algo.shortest_path(0, 6) == (30, [0, 1, 2, 3, 5, 6]))
        self.assertTrue(self.algo.shortest_path(8, 8)[0] == 0)
        self.assertTrue(len(self.algo.shortest_path(8, 8)[1]) == 1)
        self.assertTrue(self.algo.shortest_path(0, 10) == (float('inf'), []))
        self.assertTrue(self.algo.shortest_path(0, 7) == (float('inf'), []))

    def test_connected_components(self):
        self.assertTrue(len(self.algo.connected_components()) == 5)
        self.assertEqual(self.algo.connected_component(2), [self.algo.graph.get_node(2), self.algo.graph.get_node(1),
                                                            self.algo.graph.get_node(4), self.algo.graph.get_node(3)])
        self.assertTrue(self.algo.connected_component(10) == [])
        al = GraphAlgo()
        self.assertTrue(al.connected_components() == [])


if __name__ == '__main__':
    unittest.main()

