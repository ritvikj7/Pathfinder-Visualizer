import PyQt5
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView, QGraphicsEllipseItem, \
    QGraphicsRectItem, QToolBar, QAction, QPushButton, QGraphicsTextItem
from PyQt5.QtGui import QBrush, QColor, QPen, QFont
from PyQt5.QtCore import Qt, QPointF, QPoint
from math import fabs,sqrt

class Screen(QMainWindow):
    def __init__(self, map_obj):
        super().__init__()
        #booleans for determing if the head or the tail should be moved or not
        self.headchange = False
        self.tailchange = False
        #position of the head and th tail
        self.headpos = None
        self.tailpos = None


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
        # Create the navbar icon button
        self.head_icon_button = QPushButton("Head", self)
        toolbar.addWidget(self.head_icon_button)
        self.tail_icon_button = QPushButton("Tail", self)
        toolbar.addWidget(self.tail_icon_button)
        # Connect the button's clicked signal to the head or tail movement method
        self.head_icon_button.clicked.connect(self.handle_head_change)
        self.tail_icon_button.clicked.connect(self.handle_tail_change)




    #for drawing the map
    def draw_matrix(self):

        for i in range(self.num_rows):
            for j in range(self.num_cols):
                x = j * self.box_width  # Calculate the x-coordinate of the box
                y = i * self.box_height  # Calculate the y-coordinate of the box
                brush = QBrush(Qt.white)
                pen = QPen(Qt.NoPen)

                #drwing the map
                self.scene.addRect(x, y, self.box_width, self.box_height, pen, brush)


    def on_mouse_press(self, event):
        mouse_pos = event.pos()
        scene_pos = self.view.mapToScene(mouse_pos)

        x = int(scene_pos.x() // self.box_width)  # Calculate the index of the clicked box in the x-axis
        y = int(scene_pos.y() // self.box_height)  # Calculate the index of the clicked box in the y-axis

        print("Clicked at index: ({}, {})".format(x, y))

        print(scene_pos)

        clicked_item = self.scene.itemAt(scene_pos, self.view.transform())

        if isinstance(clicked_item, QGraphicsRectItem):
            if self.headchange:
                if self.map_obj.get_array()[x][y].classification == "block":
                    #check if there is head and then move or create the head
                    if self.headpos:
                        head_item = self.scene.itemAt(self.headpos, self.view.transform())
                        self.map_obj.get_array()[int(self.headpos.x() // self.box_width)][int(self.headpos.y() // self.box_height)].set_classification("block")

                        if isinstance(head_item, QGraphicsRectItem):
                            head_item.setBrush(QBrush(Qt.white))
                        # text for head

                        else:
                            b = self.headpos.y()+20
                            head_item2 = self.scene.itemAt(self.headpos.x(),b, self.view.transform())
                            head_item2.setBrush(QBrush(Qt.white))



                    else:
                        self.head_text_item = self.scene.addText("Head", QFont("Arial", 10))


                    #assign the head to the matrix
                    self.map_obj.get_array()[x][y].set_classification("head")
                    self.head_text_item.setPos((x * self.box_width) + self.box_width / 2 - self.head_text_item.boundingRect().width() / 2,
                                               (y * self.box_height) + self.box_height / 2 - self.head_text_item.boundingRect().height() / 2)

                    self.headpos = scene_pos  # assign the head position
                    clicked_item.setBrush(QBrush(Qt.green))
                    self.headchange = False

            if self.tailchange:
                if self.map_obj.get_array()[x][y].classification == "block":
                    #check if there is head and then move or create the head
                    if self.tailpos:
                        tail_item = self.scene.itemAt(self.tailpos, self.view.transform())
                        self.map_obj.get_array()[int(self.tailpos.x() // self.box_width)][int(self.tailpos.y() // self.box_height)].set_classification("block")
                        tail_item.setBrush(QBrush(Qt.white))
                        # text for tail
                        if isinstance(tail_item, QGraphicsRectItem):
                            tail_item.setBrush(QBrush(Qt.white))
                        # text for head

                        else:
                            b = self.tailpos.y()+20
                            tail_item2 = self.scene.itemAt(self.tailpos.x(),b, self.view.transform())
                            tail_item2.setBrush(QBrush(Qt.white))

                    else:
                        self.tail_text_item = self.scene.addText("Tail", QFont("Arial", 10))


                    #assign the tail to the matrix
                    self.map_obj.get_array()[x][y].set_classification("tail")
                    self.tail_text_item.setPos((x * self.box_width) + self.box_width / 2 - self.tail_text_item.boundingRect().width() / 2,
                                               (y * self.box_height) + self.box_height / 2 - self.tail_text_item.boundingRect().height() / 2)

                    self.tailpos = scene_pos  # assign the head position
                    clicked_item.setBrush(QBrush(Qt.green))
                    self.tailchange = False



            elif self.map_obj.get_array()[x][y].free and self.map_obj.get_array()[x][y].classification == "block":
                self.map_obj.get_array()[x][y].block_node()
                print(self.map_obj.get_array()[x][y].free)
                clicked_item.setBrush(QBrush(Qt.black))
            elif not self.map_obj.get_array()[x][y].free and self.map_obj.get_array()[x][y].classification == "block":
                self.map_obj.get_array()[x][y].free_node()
                print(self.map_obj.get_array()[x][y].free)
                clicked_item.setBrush(QBrush(Qt.white))

    def handle_head_change(self):
        self.headchange = not self.headchange  # Toggle the headchange variable
        self.tailchange = False
    def handle_tail_change(self):
        self.tailchange = not self.tailchange  # Toggle the headchange variable
        self.headchange = False




