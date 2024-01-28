# matplotlib_gui
This is a python module which can draw graph and histgram by GUI style.  
Please install tkinter and matplotlib before using this module.

## How to use
You need to just `import matplotlib_gui` for using this module. For instance, you type command written below in command prompt,  

>python   
>import matplotlib_gui   

then, GUI is shown on your window.

### plot
1. `import matplotlib_gui`
2. Push `sketch` button in `Graph` menubar, and write (X, Y) in a textbox, where X means width [pixel] of graph window, and Y means height of it (I usually set (800, 500)). Finary, push `sketch` button.
3. Push `create` button in `Plot` menubar.
4. Push `import` button in `Plot` menubar. Next, fill x and y coordinate values in text box. Finary you need to set `Name` for this graph which is used in legend.
5. Check `Data style` text box in `create` window. You will be able to find dataset which was imported at previous step. Next push the button `Set`, then default parameter values will be shown. Finary, pushing `draw` button, this graph is drawn.
6. Push `save` button in `Graph` menubar, and set file name (e.g, if you set "sample", sample.jpg file is written).

#### How to delete a graph
If you want to delete this dataset and graph, select the data at `Data style` and push `delete` button. Then, if you push `draw` again, the data you selected will be deleted.   
#### Scattering plot
Set `Line Width` = 0, and `Marker Type` = anything except None.

### histgram
1. `import matplotlib_gui`
2. Push `sketch` button in `Graph` menubar, and write (X, Y) in a textbox, where X means width [pixel] of graph window, and Y means height of it (I usually set (800, 500)). Finary, push `sketch` button.
3. Push `create` button in `Hist` menubar.
4. Push `import` button in `Plot` menubar. Next, write dataset values in text box. Finary you need to set `Name` for this graph which is used in legend.
5. Check `Data style` text box in `create` window. You will be able to find dataset which was imported at previous step. Next push the button `Set`, then default parameter values will be shown.
6. You need to write `bins` text box in `create` window. Sentence should be [x_min, x_max, num_bins] style (e.g., [0,10,10]).