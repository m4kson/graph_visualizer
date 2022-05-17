from tkinter import *
import tkinter.ttk as ttk

import matplotlib

matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

import networkx as nx
import matplotlib.pyplot as plt



def create_ui():
    root = Tk()
    root.geometry('1200x720')
    root.title("Graph builder")
    #todo make root not resizeable

    combobox_canvas = Canvas(root, width=150, height=75, bg='white', highlightthickness=0)
    combobox_canvas.place(x=30, y = 70)

    f = Figure(figsize=(5, 4), dpi=100)

    graph = nx.Graph()





    cities = {'A': (0, 20),
              'B': (15, 24),
              'C': (16, 41),
              'D': (10, 40)}



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







    canvs = FigureCanvasTkAgg(f, root)
    canvs.get_tk_widget().place(x=360, y=100)

    plt.show()

    graph_type = ttk.Combobox(combobox_canvas)
    graph_type.place(x = 0, y = 0)
    graph_type['values'] = ('select graph type', 'simple', 'weighted', 'directed')
    graph_type.current(0)

    action_type = ttk.Combobox(combobox_canvas)
    action_type.place(x = 0, y = 40)
    action_type['values'] = ('select action', 'build', 'dijkstra', 'breadth first search')
    action_type.current(0)

    run_button = Button(text="run", width=15, height=2, bg="green", command=test_action())
    run_button.place(x=1000, y=620)

    root.mainloop()

def test_action():
    print("run")
