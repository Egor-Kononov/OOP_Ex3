import unittest

from DiGraph import DiGraph


class MyT(unittest.TestCase):

    def test_add(self):
        g = DiGraph()
        for x in range(5):
            g.add_node(x)
        self.assertTrue(5 == g.v_size())
        self.assertFalse(g.add_node(4))

    def test_remove(self):
        g = DiGraph()
        for x in range(5):
            g.add_node(x)
        self.assertTrue(g.remove_node(4))
        self.assertFalse(g.remove_node(6))
        self.assertTrue(g.v_size() == 4)

    def test_add_edge(self):
        g = DiGraph()
        for x in range(5):
            g.add_node(x)
        self.assertTrue(g.add_edge(0, 1, 2))
        self.assertFalse(g.add_edge(0, 1, 2))
        self.assertFalse(g.add_edge(0, 6, 2))
        self.assertFalse(g.add_edge(0, 2, -2))
        self.assertTrue(g.e_size() == 1)

    def test_remove_edge(self):
        g = DiGraph()
        for x in range(5):
            g.add_node(x)
        g.add_edge(0, 1, 2)
        g.add_edge(0, 2, 2)
        g.add_edge(0, 3, 2)
        self.assertTrue(g.remove_edge(0, 1))
        self.assertFalse(g.remove_edge(0, 1))
        self.assertFalse(g.remove_edge(0, 4))

    def test_general(self):
        g = DiGraph()
        for x in range(5):
            g.add_node(x)
        g.add_edge(0, 1, 1)
        g.add_edge(0, 2, 1)
        g.add_edge(0, 3, 1)
        g.add_edge(0, 4, 1)
        g.add_edge(1, 0, 1)
        g.add_edge(1, 3, 1)
        g.add_edge(2, 0, 1)
        g.add_edge(2, 1, 1)
        g.add_edge(3, 0, 1)
        g.add_edge(3, 4, 1)
        g.add_edge(4, 0, 1)
        g.add_edge(4, 2, 1)
        self.assertTrue(g.e_size() == 12)
        self.assertTrue(g.v_size() == 5)
        self.assertTrue(g.get_mc() == 17)
        g.remove_node(0)
        self.assertTrue(g.e_size() == 4)
        self.assertTrue(g.get_mc() == 18)
        self.assertFalse(g.v_size() == 5)


if __name__ == '__main__':
    unittest.main()
