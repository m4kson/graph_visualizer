import networkx as nx
import matplotlib.pyplot as plt

cities = {'A':(0, 20),
     'B':(15, 24),
     'C':(16, 41),
     'D':(10, 40)}

graph = nx.Graph()
graph.add_nodes_from(cities)

print(graph.nodes())

def my_add_edge(f_item, s_item, graph=None):
    graph.add_edge(f_item, s_item)
    graph.add_edge(s_item, f_item)

my_add_edge('A', 'B', graph=graph)
my_add_edge('B', 'C', graph=graph)
my_add_edge('B', 'D', graph=graph)

nx.draw_circular(graph,
         node_color='red',
         node_size=1000,
         with_labels=True)

plt.show()

