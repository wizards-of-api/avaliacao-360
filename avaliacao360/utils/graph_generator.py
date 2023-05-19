import math
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import PySimpleGUI as sg

def draw_figure(canvas, figure):
    canvas = canvas.TKCanvas
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg

def generate_bar_graph(title, x_label, y_label, label_list, data, size):
    width = .25

    fig = plt.figure(figsize = size)

    plt.bar(label_list, data, color = 'maroon', width = width)

    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)

    return fig

def generate_line_graph(title, data, label_list, size):
    fig = plt.figure(figsize=size)

    colors = ['b','g','r','c','m','y','k','w']
    
    x_list = []
    y_list = []

    handles = []

    for i, coord_list in enumerate(data):
        x_args = []
        y_args = []
        for coord in coord_list:
            x_args.append(coord[0])
            y_args.append(coord[1])

            x_list.append(coord[0])
            y_list.append(coord[1])
        
        patch = mpatches.Patch(color=colors[i], label=label_list[i])
        handles.append(patch)

        plt.plot(x_args, y_args, colors[i])

    plt.legend(handles=handles)

    x_range = range(1, math.ceil(max(x_list))+1)
    y_range = range(1, math.ceil(max(y_list))+1)
    
    plt.xticks(x_range)
    plt.yticks(y_range)

    plt.title(title)
    return fig

def generate_radial_graph(title, data, label_list, size):
    fig = plt.figure(figsize =(size))
    fig.add_subplot(projection='polar')

    fix_data = data
    fix_data.append(data[0])

    theta = np.linspace(0, 2 * np.pi, len(data))

    plt.thetagrids(range(0, 360, int(360/len(label_list))), label_list)
    
    plt.plot(theta, fix_data)
    plt.fill(theta, fix_data, 'b', alpha = 0.1)

    plt.title(title)

    return fig

def generate_table(key, top_row, rows):
    return sg.Table(values=rows, headings=top_row,
   auto_size_columns=True,
   justification='center', key=key,
   expand_x=True,
   expand_y=True)