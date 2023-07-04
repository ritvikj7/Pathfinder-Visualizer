


from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView, QGraphicsEllipseItem, \
QGraphicsRectItem, QToolBar, QAction
from PyQt5.QtGui import QBrush, QColor, QPen, QFont
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
        #draw
        self.draw_matrix()
        #draw the navbar
        self.create_toolbar()
        #registering the mouse click
        self.view.mousePressEvent = self.on_mouse_press


    #The nabar code
    def create_toolbar(self):
        toolbar = QToolBar()
        self.addToolBar(toolbar)

        action1 = QAction("head", self)
        toolbar.addAction(action1)

        action2 = QAction("tail", self)
        toolbar.addAction(action2)


    #for drawing the map
    def draw_matrix(self):

        for i in range(self.num_rows):
            for j in range(self.num_cols):
                x = j * self.box_width  # Calculate the x-coordinate of the box
                y = i * self.box_height  # Calculate the y-coordinate of the box
                brush = QBrush(Qt.white)
                pen = QPen(Qt.NoPen)
                #for specifying the head or the tail
                text =""
                if self.map_obj.get_array()[j][i].classification == "head":
                    brush = QBrush(Qt.green)
                    text = "Head"

                if self.map_obj.get_array()[j][i].classification == "tail":
                    brush = QBrush(Qt.green)
                    text = "Tail"

                #drwing the map
                self.scene.addRect(x, y, self.box_width, self.box_height, pen, brush)
                #adding text to head and tails
                text_item = self.scene.addText(text, QFont("Arial", 10))
                text_item.setPos(x + self.box_width / 2 - text_item.boundingRect().width() / 2,
                                 y + self.box_height / 2 - text_item.boundingRect().height() / 2)

    def on_mouse_press(self, event):
        mouse_pos = event.pos()
        scene_pos = self.view.mapToScene(mouse_pos)

        x = int(scene_pos.x() // self.box_width)  # Calculate the index of the clicked box in the x-axis
        y = int(scene_pos.y() // self.box_height)  # Calculate the index of the clicked box in the y-axis

        print("Clicked at index: ({}, {})".format(x, y))


        clicked_item = self.scene.itemAt(scene_pos, self.view.transform())

        if isinstance(clicked_item, QGraphicsRectItem) and self.map_obj.get_array()[x][y].classification == "block":
            if self.map_obj.get_array()[x][y].free:
                self.map_obj.get_array()[x][y].block_node()
                print(self.map_obj.get_array()[x][y].free)
                clicked_item.setBrush(QBrush(Qt.black))
            else:
                self.map_obj.get_array()[x][y].free_node()
                print(self.map_obj.get_array()[x][y].free)
                clicked_item.setBrush(QBrush(Qt.white))