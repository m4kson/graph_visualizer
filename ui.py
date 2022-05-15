from tkinter import *
import tkinter.ttk as ttk

def create_ui():
    root = Tk()
    root.geometry('1200x720')
    root.title("Graph builder")

    combobox_canvas = Canvas(root, width=230, height=100, bg='white', highlightthickness=0)
    combobox_canvas.place(x=30, y = 70)

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
