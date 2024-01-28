import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def _create(app):
    window = tk.Toplevel(app)
    window.title("Attribution")
    window.geometry("620x350")

    datastyle = tk.Label(window, text = "Data style", font = ("", 10, "bold"), fg = "navy")
    datastyle.place(relx = 0.5, rely = 0.01)

    app.datalist = []
    app.data_combobox = ttk.Combobox(window, values = app.datalist)
    app.data_combobox.place(relx = 0.62, rely = 0.01)

    app.set_button = tk.Button(window, text = "Set", font = ("", 8, "bold"), fg = "red", command = app.Plot_setData)
    app.set_button.place(relx = 0.85, rely = 0.01)

    app.delete_button = tk.Button(window, text = "Delete", font = ("", 8, "bold"), fg = "blue", command = app.Plot_deleteData)
    app.delete_button.place(relx = 0.9, rely = 0.01)

    line = tk.Label(window, text = "Line", font = ("", 8, "bold"), fg = "blue")
    line.place(relx = 0.5, rely = 0.1)

    linetype = tk.Label(window, text = "Type", font = ("", 8, "bold"), fg = "darkgreen")
    linetype.place(relx = 0.55, rely = 0.1)

    app.linetype_combobox = ttk.Combobox(window, values = ("solid", "dashed", "dotted", "dashdot"))
    app.linetype_combobox.place(relx = 0.62, rely = 0.1)

    linecolor = tk.Label(window, text = "Color", font = ("", 8, "bold"), fg = "darkgreen")
    linecolor.place(relx = 0.55, rely = 0.17)

    color_variation = (
		"black",
		"grey",
		"lightgray",
		"white",
		"darkred",
		"green",
		"cyan",
		"blue",
		"darkviolet",
		"magenta",
		"brown",
		"red",
		"gold",
		"lime",
		"navy",
		"purple",
		"yellow",
		"darkgreen"
		)
    
    app.linecolor_combobox = ttk.Combobox(window, values = color_variation)
    app.linecolor_combobox.place(relx = 0.62, rely = 0.17)

    linewidth = tk.Label(window, text = "Width", font = ("", 8, "bold"), fg = "darkgreen")
    linewidth.place(relx = 0.55, rely = 0.24)

    app.linewidth_text = tk.Entry(window)
    app.linewidth_text.place(relx = 0.62, rely = 0.24)

    marker = tk.Label(window, text = "Marker", font = ("", 8, "bold"), fg = "blue")
    marker.place(relx = 0.50, rely = 0.31)

    markertype = tk.Label(window, text = "Type", font = ("", 8, "bold"), fg = "darkgreen")
    markertype.place(relx = 0.55, rely = 0.38)

    marker_variation = (
		"None",
		".",
		",",
		"o",
		"v",
		"^",
		"<",
		">",
		"x",
		"+"
		)
    
    app.markertype_combobox = ttk.Combobox(window, values = marker_variation)
    app.markertype_combobox.place(relx = 0.62, rely = 0.38)

    markersize = tk.Label(window, text = "Size", font = ("", 8, "bold"), fg = "darkgreen")
    markersize.place(relx = 0.55, rely = 0.45)
    app.markersize_text = tk.Entry(window)
    app.markersize_text.place(relx = 0.62, rely = 0.45)

    markercolor = tk.Label(window, text = "Color", font = ("", 8, "bold"), fg = "darkgreen")
    markercolor.place(relx = 0.55, rely = 0.52)

    app.markercolor_combobox = ttk.Combobox(window, values = color_variation)
    app.markercolor_combobox.place(relx = 0.62, rely = 0.52)

    markeredgewidth = tk.Label(window, text = "width", font = ("", 8, "bold"), fg = "darkgreen")
    markeredgewidth.place(relx = 0.55, rely = 0.59)

    app.markeredgewidth_text = tk.Entry(window)
    app.markeredgewidth_text.place(relx = 0.62, rely = 0.59)

    markeredgecolor = tk.Label(window, text = "Edge color", font = ("", 8, "bold"), fg = "darkgreen")
    markeredgecolor.place(relx = 0.55, rely = 0.66)

    app.markeredgecolor_combobox = ttk.Combobox(window, values = color_variation)
    app.markeredgecolor_combobox.place(relx = 0.65, rely = 0.66)

    alpha = tk.Label(window, text = "Alpha", font = ("", 8, "bold"), fg = "blue")
    alpha.place(relx = 0.5, rely = 0.73)

    app.alpha_text = tk.Entry(window)
    app.alpha_text.place(relx = 0.62, rely = 0.73)

    update_button = tk.Button(window, text = "Update",
    font = ("", 8, "bold"), fg = "red", command = app.Plot_updateStyle)
    update_button.place(relx = 0.62, rely = 0.85)

    app.draw_button = tk.Button(window, text = "Draw", font = ("", 10, "bold"), fg = "red", command = app.Plot_draw)
    app.draw_button.place(relx = 0.85, rely = 0.85)

    Graphstyle = tk.Label(window, text = "Graph style", font = ("", 10, "bold"), fg = "navy")
    Graphstyle.place(relx = 0., rely = 0.01)

    xrange_label = tk.Label(window, text = "X range", font = ("", 8, "bold"), fg = "blue")
    xrange_label.place(relx = 0.01, rely = 0.1)
    app.xrange_text = tk.Entry(window)
    app.xrange_text.place(relx = 0.1, rely = 0.1)

    yrange_label = tk.Label(window, text = "Y range", font = ("", 8, "bold"), fg = "blue")
    yrange_label.place(relx = 0.01, rely = 0.17)
    app.yrange_text = tk.Entry(window)
    app.yrange_text.place(relx = 0.1, rely = 0.17)

    log_label = tk.Label(window, text = "logscale", font = ("", 8, "bold"), fg = "blue")
    log_label.place(relx = 0.01, rely = 0.24)
    app.log_combobox = ttk.Combobox(window, values = ("None", "X", "Y", "All"))
    app.log_combobox.place(relx = 0.1, rely = 0.24)

    x_label = tk.Label(window, text = "X label", font = ("", 8, "bold"), fg = "blue")
    x_label.place(relx = 0.01, rely = 0.31)
    app.x_label_text = tk.Entry(window)
    app.x_label_text.place(relx = 0.1, rely = 0.31)

    y_label = tk.Label(window, text = "Y label", font = ("", 8, "bold"), fg = "blue")
    y_label.place(relx = 0.01, rely = 0.38)
    app.y_label_text = tk.Entry(window)
    app.y_label_text.place(relx = 0.1, rely = 0.38)

    grid_label = tk.Label(window, text = "Grid", font = ("", 8, "bold"), fg = "blue")
    grid_label.place(relx = 0.01, rely = 0.45)
    app.grid_button = tk.IntVar()
    app.grid_button.set(1)

    off_grid_button = tk.Radiobutton(window, text = "off", value = 1, variable = app.grid_button)
    on_grid_button = tk.Radiobutton(window, text = "on", value = 2, variable = app.grid_button)
    off_grid_button.place(relx = 0.1, rely = 0.45)
    on_grid_button.place(relx = 0.2, rely = 0.45)

    legend_label = tk.Label(window, text = "Legend", font = ("", 10, "bold"), fg = "navy")
    legend_label.place(relx = 0., rely = 0.52)
    app.legend_button = tk.IntVar()
    app.legend_button.set(1)
    off_button = tk.Radiobutton(window, text = "off", value = 1, variable = app.legend_button)
    on_button = tk.Radiobutton(window, text = "on", value = 2, variable = app.legend_button)
    off_button.place(relx = 0.1, rely = 0.52)
    on_button.place(relx = 0.2, rely = 0.52)


def _setData(app):
    pass

def _deleteData(app):
    pass

def _updateStyle(app):
    pass

def _draw(app):
    pass