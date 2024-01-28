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

	app.set_button = tk.Button(window, text = "Set", font = ("", 8, "bold"), fg = "red", command = app.Hist_setData)
	app.set_button.place(relx = 0.85, rely = 0.01)

	app.delete_button = tk.Button(window, text = "Delete", font = ("", 8, "bold"), fg = "blue", command = app.Hist_deleteData)
	app.delete_button.place(relx = 0.9, rely = 0.01)

	color = tk.Label(window, text = "Color", font = ("", 8, "bold"), fg = "blue")
	color.place(relx = 0.55, rely = 0.1)

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

	app.color_combobox = ttk.Combobox(window, values = color_variation)
	app.color_combobox.place(relx = 0.62, rely = 0.1)

	linewidth = tk.Label(window, text = "Width", font = ("", 8, "bold"), fg = "blue")
	linewidth.place(relx = 0.55, rely = 0.17)
	app.linewidth_text = tk.Entry(window)
	app.linewidth_text.place(relx = 0.62, rely = 0.17)

	edgecolor = tk.Label(window, text = "Edgecolor", font = ("", 8, "bold"), fg = "blue")
	edgecolor.place(relx = 0.55, rely = 0.24)
	app.edgecolor_combobox = ttk.Combobox(window, values = color_variation)
	app.edgecolor_combobox.place(relx = 0.65, rely = 0.24)

	alpha = tk.Label(window, text = "Alpha", font = ("", 8, "bold"), fg = "blue")
	alpha.place(relx = 0.55, rely = 0.31)
	app.alpha_text = tk.Entry(window)
	app.alpha_text.place(relx = 0.62, rely = 0.31)

	update_button = tk.Button(window, text = "Update", font = ("", 10, "bold"), fg = "red", command = app.Hist_updateStyle)
	update_button.place(relx = 0.62, rely = 0.41)


	app.draw_button = tk.Button(window, text = "Draw", font = ("", 10, "bold"), fg = "red", command = app.Hist_draw)
	app.draw_button.place(relx = 0.85, rely = 0.41)

	Graphstyle = tk.Label(window, text = "Graph style", font = ("", 10, "bold"), fg = "navy")
	Graphstyle.place(relx = 0., rely = 0.01)

	x_label = tk.Label(window, text = "X label", font = ("", 8, "bold"), fg = "blue")
	x_label.place(relx = 0.01, rely = 0.1)
	app.x_label_text = tk.Entry(window)
	app.x_label_text.place(relx = 0.1, rely = 0.1)

	y_label = tk.Label(window, text = "Y label", font = ("", 8, "bold"), fg = "blue")
	y_label.place(relx = 0.01, rely = 0.17)
	app.y_label_text = tk.Entry(window)
	app.y_label_text.place(relx = 0.1, rely = 0.17)

	bins_label = tk.Label(window, text = "bins", font = ("", 10, "bold"), fg = "navy")
	bins_label.place(relx = 0., rely = 0.24)
	app.bins_text = tk.Entry(window)
	app.bins_text.place(relx = 0.1, rely = 0.24)

	norm_label = tk.Label(window, text = "norm", font = ("", 10, "bold"), fg = "navy")
	norm_label.place(relx = 0., rely = 0.31)
	app.norm_button = tk.IntVar()
	app.norm_button.set(0)
	off_norm_button = tk.Radiobutton(window, text = "off", value = 0, variable = app.norm_button)
	on_norm_button = tk.Radiobutton(window, text = "on", value = 1, variable = app.norm_button)
	off_norm_button.place(relx = 0.15, rely = 0.31)
	on_norm_button.place(relx = 0.25, rely = 0.31)

	cumulative_label = tk.Label(window, text = "cumulative", font = ("", 10, "bold"), fg = "navy")
	cumulative_label.place(relx = 0., rely = 0.38)
	app.cumulative_button = tk.IntVar()
	app.cumulative_button.set(0)
	off_cumulative_button = tk.Radiobutton(window, text = "off", value = 0, variable = app.cumulative_button)
	on_cumulative_button = tk.Radiobutton(window, text = "on", value = 1, variable = app.cumulative_button)
	off_cumulative_button.place(relx = 0.15, rely = 0.38)
	on_cumulative_button.place(relx = 0.25, rely = 0.38)

	stack_label = tk.Label(window, text = "stack", font = ("", 10, "bold"), fg = "navy")
	stack_label.place(relx = 0., rely = 0.45)
	app.stack_button = tk.IntVar()
	app.stack_button.set(0)
	off_stack_button = tk.Radiobutton(window, text = "off", value = 0, variable = app.stack_button)
	on_stack_button = tk.Radiobutton(window, text = "on", value = 1, variable = app.stack_button)
	off_stack_button.place(relx = 0.15, rely = 0.45)
	on_stack_button.place(relx = 0.25, rely = 0.45)

	legend_label = tk.Label(window, text = "Legend", font = ("", 10, "bold"), fg = "navy")
	legend_label.place(relx = 0., rely = 0.52)
	app.legend_button = tk.IntVar()
	app.legend_button.set(0)
	off_button = tk.Radiobutton(window, text = "off", value = 0, variable = app.legend_button)
	on_button = tk.Radiobutton(window, text = "on", value = 1, variable = app.legend_button)
	off_button.place(relx = 0.15, rely = 0.52)
	on_button.place(relx = 0.25, rely = 0.52)

	xrange_label = tk.Label(window, text = "X range", font = ("", 8, "bold"), fg = "blue")
	xrange_label.place(relx = 0., rely = 0.59)
	app.xrange_text = tk.Entry(window)
	app.xrange_text.place(relx = 0.1, rely = 0.59)

	yrange_label = tk.Label(window, text = "Y range", font = ("", 8, "bold"), fg = "blue")
	yrange_label.place(relx = 0., rely = 0.66)
	app.yrange_text = tk.Entry(window)
	app.yrange_text.place(relx = 0.1, rely = 0.66)

def getBins(app):
	bins = app.bins_text.get()
	if bins[0] == "[":
		bins = bins[1:-1]
		bins = bins.split(",")
		bins = np.array(bins).astype(float)
		width = bins[1]-bins[0]
		bins = np.arange(bins[0], bins[1]+width/bins[2], width/bins[2])
	else:
		bins = int(bins)

	return bins

def export_Range(string):
	string = string[1:-1]
	string = string.split(",")
	string = np.array(string).astype(float)

	return string

def _draw(app):
	app.plot.cla()

	if app.legend_button.get() == 0:
		for dataset in app.Datasets:
			app.plot.hist(dataset["X"],
				bins = getBins(app),
				density = app.norm_button.get(),
				cumulative = app.cumulative_button.get(),
				stacked = app.stack_button.get(),
				color = dataset["color"],
				ec = dataset["edgecolor"],
				linewidth = dataset["linewidth"],
				alpha = dataset["alpha"])

	else:
		for dataset in app.Datasets:
			app.plot.hist(dataset["X"],
				bins = getBins(app),
				density = app.norm_button.get(),
				cumulative = app.cumulative_button.get(),
				stacked = app.stack_button.get(),
				label = dataset["name"],
				color = dataset["color"],
				ec = dataset["edgecolor"],
				linewidth = dataset["linewidth"],
				alpha = dataset["alpha"])

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
	app.plot.set_xlabel(app.x_label_text.get(), fontsize = 12)
	app.plot.set_ylabel(app.y_label_text.get(), fontsize = 12)

	app.canvas = FigureCanvasTkAgg(app.figure, app.graph_window)
	app.canvas.get_tk_widget().place(relx = 0.0, rely = 0.0)

def _setData(app):
	data_name = app.data_combobox.get()

	for datasets in app.Datasets:
		if data_name == datasets["name"]:
			app.color_combobox.set(datasets["color"])
			app.linewidth_text.delete(0, tk.END)
			app.linewidth_text.insert(tk.END, datasets["linewidth"])
			app.alpha_text.delete(0, tk.END)
			app.alpha_text.insert(tk.END, datasets["alpha"])
			app.edgecolor_combobox.set(datasets["edgecolor"])

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

def _import(app):
	window = tk.Toplevel(app)
	window.title("Import data")
	window.geometry("200x450")
	x = tk.Label(window, text = "X", font = ("", 10, "bold"), fg = "navy")
	Name = tk.Label(window, text = "Name", font = ("", 10, "bold"), fg = "navy")
	x.place(relx = 0.1, rely = 0.05)
	Name.place(relx = 0.1, rely = 0.75)
	x_text = tk.Text(window, width = 15, height = 20)
	Name_text = tk.Entry(window)
	x_text.place(relx = 0.1, rely = 0.1)
	Name_text.place(relx = 0.35, rely = 0.75)

	def Import_Button():
		x_data = x_text.get("1.0", "end-1c")
		x_data = x_data.split("\n")
		x_data = np.array(x_data).astype(float)

		name = Name_text.get()

		dataset = return_Dataset(x_data, name)

		if app.Datasets is None:
			app.Datasets = [dataset]
		else:
			app.Datasets.append(dataset)

		app.datalist.append(name)
		app.data_combobox["values"] = app.datalist

		window.destroy()

	import_button = tk.Button(window, text = "Import", command = Import_Button)
	import_button.place(relx = 0.6, rely = 0.9)

def return_Dataset(X, name):
	dataset = {
	"name" : name,
	"X" : X,
	"color" : "black",
	"edgecolor" : "black",
	"linewidth" : 1.,
	"alpha" : 1.0
	}

	return dataset


def _updateStyle(app):
	data_name = app.data_combobox.get()

	for dataset in app.Datasets:
		if dataset["name"] == data_name:
			dataset["color"] = app.color_combobox.get()
			dataset["linewidth"] = float(app.linewidth_text.get())
			dataset["alpha"] = float(app.alpha_text.get())
			dataset["edgecolor"] = app.edgecolor_combobox.get()

			break