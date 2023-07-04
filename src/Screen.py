


from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView, QGraphicsEllipseItem, \
QGraphicsRectItem, QToolBar, QAction
from PyQt5.QtGui import QBrush, QColor, QPen
from PyQt5.QtCore import Qt, QPointF

class Screen(QMainWindow):
    def __init__(self, map_obj):
        super().__init__()

        self.setWindowTitle("Matrix Visualization")

        self.scene = QGraphicsScene()
        self.view = QGraphicsView(self.scene)

        self.setCentralWidget(self.view)

        self.map_obj = map_obj

        self.num_rows = 10
        self.num_cols = 10

        # Calculate the size of each box
        self.box_width = self.view.width() / self.num_cols
        self.box_height = self.view.height() / self.num_rows

        self.draw_matrix()
        self.create_toolbar()
        self.view.mousePressEvent = self.on_mouse_press


    def create_toolbar(self):
        toolbar = QToolBar()
        self.addToolBar(toolbar)

        action1 = QAction("Action 1", self)
        toolbar.addAction(action1)

        action2 = QAction("Action 2", self)
        toolbar.addAction(action2)



    def draw_matrix(self):

        for i in range(self.num_rows):
            for j in range(self.num_cols):
                x = j * self.box_width  # Calculate the x-coordinate of the box
                y = i * self.box_height  # Calculate the y-coordinate of the box

                brush = QBrush(Qt.white)
                pen = QPen(Qt.NoPen)

                self.scene.addRect(x, y, self.box_width, self.box_height, pen, brush)

    def on_mouse_press(self, event):
        mouse_pos = event.pos()
        scene_pos = self.view.mapToScene(mouse_pos)

        x = int(scene_pos.x() // self.box_width)  # Calculate the index of the clicked box in the x-axis
        y = int(scene_pos.y() // self.box_height)  # Calculate the index of the clicked box in the y-axis

        print("Clicked at index: ({}, {})".format(x, y))


        clicked_item = self.scene.itemAt(scene_pos, self.view.transform())

        if isinstance(clicked_item, QGraphicsRectItem):
            if self.map_obj.get_array()[x][y].free and self.map_obj.get_array()[x][y].classification == "regular":
                self.map_obj.get_array()[x][y].block_node()
                print(self.map_obj.get_array()[x][y].free)
                clicked_item.setBrush(QBrush(Qt.black))
            else:
                self.map_obj.get_array()[x][y].free_node()
                print(self.map_obj.get_array()[x][y].free)
                clicked_item.setBrush(QBrush(Qt.white))