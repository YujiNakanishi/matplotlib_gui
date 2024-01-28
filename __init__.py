import tkinter as tk
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from matplotlib_gui import Graph_Menu

__version__ = 1.0

class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        master.title("graf")
        master.geometry("640x0")
        self.pack()
        self.Datasets = None
        createMenu(self)

    def sketch(self): Graph_Menu.sketch(self)
    def save(self): Graph_Menu._save(self)

def createMenu(app):
    menubar = tk.Menu(app)
    app.master["menu"] = menubar

    Graph_menu = tk.Menu(menubar, tearoff = False)
    Graph_menu.add_command(label = "sketch", command = app.sketch)
    Graph_menu.add_command(label = "save image", command = app.save)
    menubar.add_cascade(label = "Graph", menu = Graph_menu)

root = tk.Tk(); app = Application(root)