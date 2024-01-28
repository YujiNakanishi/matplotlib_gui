import tkinter as tk
import numpy as np
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def sketch(app):
    window = tk.Toplevel(app)
    window.title("Sketch")
    window.geometry("250x100")
    filename = tk.Label(window, text = "Figure ratio", font = ("", 10, "bold"), fg = "navy")
    filename.place(relx = 0., rely = 0.05)
    Name_text = tk.Entry(window)
    Name_text.place(relx = 0.1, rely = 0.4)

    def save_Button():        
        string = Name_text.get()
        string = string[1:-1]
        string = string.split(",")
        string = np.array(string).astype(float)
        app.xsize = string[0]; app.ysize = string[1]

        app.graph_window = tk.Toplevel(app)
        app.graph_window.title("graph window")
        app.graph_window.geometry(str(int(app.xsize+10))+"x"+str(int(app.ysize+10)))

        app.figure = Figure(figsize = (int(app.xsize/100), int(app.ysize/100)), dpi = 100)
        app.figure.subplots_adjust(left=0.2, bottom=0.2, right=0.95, top=0.95)
        app.plot = app.figure.add_subplot(111)
        app.canvas = FigureCanvasTkAgg(app.figure, app.graph_window)
        app.canvas.get_tk_widget().place(relx = 0.0, rely = 0.0)

        window.destroy()
    
    save_button = tk.Button(window, text = "Sketch", command = save_Button)
    save_button.place(relx = 0.8, rely = 0.7)