import unittest

from DiGraph import DiGraph


class MyT(unittest.TestCase):

    def setUp(self) -> None:
        self.g = DiGraph()
        for x in range(5):
            self.g.add_node(x)

    def test_add(self):
        self.assertTrue(5 == self.g.v_size())
        self.assertFalse(self.g.add_node(4))

    def test_remove(self):
        self.assertTrue(self.g.remove_node(4))
        self.assertFalse(self.g.remove_node(6))
        self.assertTrue(self.g.v_size() == 4)

    def test_add_edge(self):
        self.assertTrue(self.g.add_edge(0, 1, 2))
        self.assertFalse(self.g.add_edge(0, 1, 2))
        self.assertFalse(self.g.add_edge(0, 6, 2))
        self.assertFalse(self.g.add_edge(0, 2, -2))
        self.assertTrue(self.g.e_size() == 1)

    def test_remove_edge(self):
        self.g.add_edge(0, 1, 2)
        self.g.add_edge(0, 2, 2)
        self.g.add_edge(0, 3, 2)
        self.assertTrue(self.g.remove_edge(0, 1))
        self.assertFalse(self.g.remove_edge(0, 1))
        self.assertFalse(self.g.remove_edge(0, 4))

    def test_general(self):
        self.g.add_edge(0, 1, 1)
        self.g.add_edge(0, 2, 1)
        self.g.add_edge(0, 3, 1)
        self.g.add_edge(0, 4, 1)
        self.g.add_edge(1, 0, 1)
        self.g.add_edge(1, 3, 1)
        self.g.add_edge(2, 0, 1)
        self.g.add_edge(2, 1, 1)
        self.g.add_edge(3, 0, 1)
        self.g.add_edge(3, 4, 1)
        self.g.add_edge(4, 0, 1)
        self.g.add_edge(4, 2, 1)
        self.assertTrue(self.g.e_size() == 12)
        self.assertTrue(self.g.v_size() == 5)
        self.assertTrue(self.g.get_mc() == 17)
        self.g.remove_node(0)
        self.assertTrue(self.g.e_size() == 4)
        self.assertTrue(self.g.get_mc() == 18)
        self.assertFalse(self.g.v_size() == 5)


if __name__ == '__main__':
    unittest.main()
