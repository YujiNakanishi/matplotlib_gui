import tkinter as tk
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

__version__ = 1.0

class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        master.title("graf")
        master.geometry("640x0")
        self.pack()
        self.Datasets = None
        createMenu(self)

def createMenu(app):
    menubar = tk.Menu(app)
    app.master["menu"] = menubar

root = tk.Tk(); app = Application(root)