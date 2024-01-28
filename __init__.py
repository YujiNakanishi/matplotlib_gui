"""
GUI for drawing graph by matplotlib.

# How to use.
---Just importing matplotlib_gui---

For instance, you command "import matplotlib_gui" on command prompt.
>>>python
>>>import matplotlib_gui

Then, GUI window will be created!
"""

import tkinter as tk
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from matplotlib_gui import Graph_Menu
from matplotlib_gui import Plot
from matplotlib_gui import Hist

class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        master.title("matplotlib_gui")
        master.geometry("640x0")
        self.pack()
        self.Datasets = None
        createMenu(self)

    """
    functions for "Graph" menu bar.
    If you want to add a new function, please add it here and "Graph_Menu.py"
    """
    def sketch(self): Graph_Menu.sketch(self)
    def save(self): Graph_Menu._save(self)

    """
    functions for "Plot" menu bar.
    If you want to add a new function, please add it here and "Plot.py"
    """
    def Plot_create(self): Plot._create(self)
    def Plot_setData(self): Plot._setData(self)
    def Plot_deleteData(self): Plot._deleteData(self)
    def Plot_updateStyle(self): Plot._updateStyle(self)
    def Plot_draw(self): Plot._draw(self)
    def Plot_import(self): Plot._import(self)
    def Plot_fillimport(self): Plot._fillimport(self)

    """
    functions for "Hist" menu bar.
    If you want to add a new function, please add it here and "Hist.py"
    """
    def Hist_create(self): Hist._create(self)
    def Hist_setData(self): Hist._setData(self)
    def Hist_deleteData(self): Hist._deleteData(self)
    def Hist_draw(self): Hist._draw(self)
    def Hist_import(self): Hist._import(self)
    def Hist_updateStyle(self): Hist._updateStyle(self)



def createMenu(app):
    menubar = tk.Menu(app)
    app.master["menu"] = menubar

    Graph_menu = tk.Menu(menubar, tearoff = False)
    Graph_menu.add_command(label = "sketch", command = app.sketch)
    Graph_menu.add_command(label = "save image", command = app.save)
    menubar.add_cascade(label = "Graph", menu = Graph_menu)


    Plot_menu = tk.Menu(menubar, tearoff = False)
    Plot_menu.add_command(label = "create", command = app.Plot_create)
    Plot_menu.add_command(label = "import", command = app.Plot_import)
    Plot_menu.add_command(label = "fill import", command = app.Plot_fillimport)
    menubar.add_cascade(label = "Plot", menu = Plot_menu)


    Hist_menu = tk.Menu(menubar, tearoff = False)
    Hist_menu.add_command(label = "create", command = app.Hist_create)
    Hist_menu.add_command(label = "import", command = app.Hist_import)
    menubar.add_cascade(label = "Hist", menu = Hist_menu)

root = tk.Tk(); app = Application(root)