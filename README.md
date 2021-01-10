# Directed Weighted Graph

1 [What is this project"?](#login-optional-fields)

2 [basic algorithms](#login-optional-fields-2)

3 [how does a directed floating graph visually look like](#login-optional-fields-3)

<h4 id="login-optional-fields">

# What is this project"?

</h4>

This project presents a directed weighted graph written using the language *Python*  ,you can take advantage of main functions like *short_path* in order to find the shortest path,
*plot_graph* to visually see the graph and connected_components,connected_component to finds all the Strongly Connected Component(SCC) in the graph.


<h4 id="login-optional-fields-2">

# basic algorithms

</h4>
Tarjan's algorithm-The algorithm takes a directed graph as input, and produces a partition of the graph's vertices into the graph's strongly connected components. Each vertex of the graph appears in exactly one of the strongly connected components. Any vertex that is not on a directed cycle forms a strongly connected component all by itself: for example, a vertex whose in-degree or out-degree is 0, or any vertex of an acyclic graph.

The basic idea of the algorithm is this: a depth-first search (DFS) begins from an arbitrary start node (and subsequent depth-first searches are conducted on any nodes that have not yet been found). As usual with depth-first search, the search visits every node of the graph exactly once, declining to revisit any node that has already been visited. Thus, the collection of search trees is a spanning forest of the graph. The strongly connected components will be recovered as certain subtrees of this forest. The roots of these subtrees are called the "roots" of the strongly connected components. Any node of a strongly connected component might serve as a root, if it happens to be the first node of a component that is discovered by search https://en.wikipedia.org/wiki/Tarjan%27s_strongly_connected_components_algorithm

![](https://github.com/Guppi4/Ex3_python/blob/main/Algorithm_Tarjan.png?raw=true)

Dijkstra's algorithm-  is an algorithm for finding the shortest paths between nodes in a graph, which may represent, for example, road networks. It was conceived by computer scientist Edsger W. Dijkstra in 1956 and published three years later.[5][6][7]

The algorithm exists in many variants. Dijkstra's original algorithm found the shortest path between two given nodes,[7] but a more common variant fixes a single node as the "source" node and finds shortest paths from the source to all other nodes in the graph, producing a shortest-path tree.
https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/

![](https://github.com/Guppi4/Ex3_python/blob/main/Dijkstra-Algorithm-Step-7.png?raw=true)


# How does a directed floating graph visually look like
<h4 id="login-optional-fields-3">
 ![](https://github.com/Guppi4/Ex3_python/blob/main/2.PNG?raw=true)



</h4>





