import tkinter as tk
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from matplotlib_gui import Graph_Menu
from matplotlib_gui import Plot

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


    def Plot_create(self): Plot._create(self)
    def Plot_setData(self): Plot._setData(self)
    def Plot_deleteData(self): Plot._deleteData(self)
    def Plot_updateStyle(self): Plot._updateStyle(self)
    def Plot_draw(self): Plot._draw(self)
    def Plot_import(self): Plot._import(self)

def createMenu(app):
    menubar = tk.Menu(app)
    app.master["menu"] = menubar

    Graph_menu = tk.Menu(menubar, tearoff = False)
    Graph_menu.add_command(label = "sketch", command = app.sketch)
    Graph_menu.add_command(label = "save image", command = app.save)
    menubar.add_cascade(label = "Graph", menu = Graph_menu)


    Plot_menu = tk.Menu(menubar, tearoff = False)
    Plot_menu.add_command(label = "create", command = app.Plot_create)
    menubar.add_cascade(label = "Plot", menu = Plot_menu)

root = tk.Tk(); app = Application(root)