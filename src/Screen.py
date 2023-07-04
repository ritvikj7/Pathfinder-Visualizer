from map.Node import Node
from map.Map import Map
import matplotlib.pyplot as plt
import tkinter as tk


def screen():
    map_obj = Map()
    x_coords = []
    y_coords = []

    for i in range(9):
        for j in range(9):
            x_coords.append(map_obj.get_array()[i][j].x)
            y_coords.append(map_obj.get_array()[i][j].y)

    # Plot the matrix as a grid using matplotlib
    plt.plot(x_coords, y_coords, 'o')
    plt.grid(True)
    plt.show()

    # Create a simple UI using tkinter to display the matrix
    root = tk.Tk()
    root.title("Matrix Visualization")

    # Create a canvas to draw the matrix
    canvas = tk.Canvas(root, width=500, height=500)
    canvas.pack()

    # Draw the matrix on the canvas
    for i in range(9):
        for j in range(9):
            x = map_obj.get_array()[i][j].x
            y = map_obj.get_array()[i][j].y
    canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill="black")

    root.mainloop()

