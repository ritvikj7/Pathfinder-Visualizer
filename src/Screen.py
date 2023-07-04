


from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView, QGraphicsEllipseItem, \
    QGraphicsRectItem, QToolBar, QAction, QPushButton, QGraphicsTextItem
from PyQt5.QtGui import QBrush, QColor, QPen, QFont
from PyQt5.QtCore import Qt, QPointF

class Screen(QMainWindow):
    def __init__(self, map_obj):
        super().__init__()
        #booleans for determing if the head or the tail should be moved or not
        self.headchange = False
        self.tailchange = False
        #position of the head and th tail
        self.headpos =[]
        self.tailpos =[]
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
                #for specifying the head or the tail
                text =""
                if self.map_obj.get_array()[i][j].classification == "head":
                    self.headpos.append(j)
                    self.headpos.append(i)
                    brush = QBrush(Qt.green)
                    text = "Head"


                if self.map_obj.get_array()[i][j].classification == "tail":
                    self.tailpos.append(j)
                    self.tailpos.append(i)
                    brush = QBrush(Qt.green)
                    text = "Tail"



                #drwing the map
                self.scene.addRect(x, y, self.box_width, self.box_height, pen, brush)
                #adding text
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

        if isinstance(clicked_item, QGraphicsRectItem):
            if self.headchange:
                if self.map_obj.get_array()[x][y].classification == "block":

                    # Move the head block
                    print(self.headpos)
                    head_item = self.scene.itemAt(self.headpos[0], self.headpos[1], self.view.transform())
                    head_item.setBrush(QBrush(Qt.white))
                    text_item = self.scene.itemAt(self.headpos[0] * self.box_width, self.headpos[1] * self.box_height, self.view.transform())
                    if isinstance(text_item, QGraphicsTextItem):
                        # Remove the text item from the scene
                        self.scene.removeItem(text_item)

                    # Update the position of the rectangle item
                    clicked_item.setRect(x * self.box_width, y * self.box_height, self.box_width, self.box_height)
                    clicked_item.setBrush(QBrush(Qt.green))

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




