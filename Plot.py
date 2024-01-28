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
    data_name = app.data_combobox.get()
    for datasets in app.Datasets:
        if data_name == datasets["name"]:
            app.linetype_combobox.set(datasets["linetype"])
            app.linecolor_combobox.set(datasets["linecolor"])
            app.markertype_combobox.set(datasets["markertype"])
            app.linewidth_text.delete(0, tk.END)
            app.linewidth_text.insert(tk.END, datasets["linewidth"])
            app.markersize_text.delete(0, tk.END)
            app.markersize_text.insert(tk.END, datasets["markersize"])
            app.alpha_text.delete(0, tk.END)
            app.alpha_text.insert(tk.END, datasets["alpha"])
            app.markercolor_combobox.set(datasets["markercolor"])
            app.markeredgecolor_combobox.set(datasets["markeredgecolor"])
            app.markeredgewidth_text.delete(0, tk.END)
            app.markeredgewidth_text.insert(tk.END, datasets["markeredgewidth"])

            break

def _deleteData(app):
    data_name = app.data_combobox.get()
    app.data_combobox.set("")

    app.datalist.remove(data_name)
    app.data_combobox["values"] = app.datalist

    new_Datasets = []

    for dataset in app.Datasets:
        if dataset["name"] != data_name:
            new_Datasets.append(dataset)

    app.Datasets = new_Datasets

def _updateStyle(app):
    pass


def export_Range(string):
    string = string[1:-1]
    string = string.split(",")
    string = np.array(string).astype(float)

    return string

def _draw(app):
    app.plot.cla()

    if app.legend_button.get() == 1:
        for dataset in app.Datasets:
            if dataset["type"] == "fill_import":
                app.plot.fill_between(dataset["X"], dataset["Y"][0], dataset["Y"][1], 
                color = dataset["linecolor"],
                alpha = dataset["alpha"])
            else:
                app.plot.plot(dataset["X"], dataset["Y"], 
                linestyle = dataset["linetype"],
                color = dataset["linecolor"],
                marker = dataset["markertype"],
                markersize = dataset["markersize"],
                markerfacecolor = dataset["markercolor"],
                markeredgecolor = dataset["markeredgecolor"],
                markeredgewidth = dataset["markeredgewidth"],
                linewidth = dataset["linewidth"],
                alpha = dataset["alpha"])
    else:
        for dataset in app.Datasets:
            if dataset["type"] == "fill_import":
                app.plot.fill_between(dataset["X"], dataset["Y"][0], dataset["Y"][1], 
                color = dataset["linecolor"],
                alpha = dataset["alpha"],
                label = dataset["name"])
            else:
                app.plot.plot(dataset["X"], dataset["Y"], 
                linestyle = dataset["linetype"],
                color = dataset["linecolor"],
                marker = dataset["markertype"],
                markersize = dataset["markersize"],
                markerfacecolor = dataset["markercolor"],
                markeredgecolor = dataset["markeredgecolor"],
                markeredgewidth = dataset["markeredgewidth"],
                linewidth = dataset["linewidth"],
                alpha = dataset["alpha"],
                label = dataset["name"])

        app.plot.legend(loc = "best")

    x_range = app.xrange_text.get()
    if x_range != "":
        x_range = export_Range(x_range) #np配列。
        app.plot.set_xlim(x_range[0], x_range[1])

    y_range = app.yrange_text.get()
    if y_range != "":
        y_range = export_Range(y_range) #np配列。
        app.plot.set_ylim(y_range[0], y_range[1])
	
    app.plot.set_xlabel(app.x_label_text.get(), fontsize = 12)
    app.plot.set_ylabel(app.y_label_text.get(), fontsize = 12)

    log = app.log_combobox.get()
    if log == "X":
        app.plot.set_xscale("log")
        app.plot.set_yscale("linear")
    elif log == "Y":
        app.plot.set_xscale("linear")
        app.plot.set_yscale("log")
    elif log == "All":
        app.plot.set_xscale("log")
        app.plot.set_yscale("log")
    else:
        app.plot.set_xscale("linear")
        app.plot.set_yscale("linear")

    app.plot.grid((app.grid_button.get() == 2), which = "major", axis = "both")
    app.canvas = FigureCanvasTkAgg(app.figure, app.graph_window)
    app.canvas.get_tk_widget().place(relx = 0.0, rely = 0.0)