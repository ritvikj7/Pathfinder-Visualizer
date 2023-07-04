
import tkinter as tk
import matplotlib.pyplot as plt


class Screen:
    def __int__(self):
        pass

    def showscreen(self, map_obj):
        root = tk.Tk()
        root.title("Matrix Visualization")

        # Create a canvas to draw the matrix
        canvas = tk.Canvas(root, width=500, height=500)
        canvas.pack()

        # Draw the matrix on the canvas
        for i in range(500):
            for j in range(500):
                if(map_obj.get_array()[i][j].)
                canvas.create_oval(map_obj.get_array()[i][j].x - 5, map_obj.get_array()[i][j].y - 5, map_obj.get_array()[i][j].x + 5, map_obj.get_array()[i][j].y + 5, fill="black")

        root.mainloop()
