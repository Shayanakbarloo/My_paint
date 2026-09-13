import sys # this will bring in python's built-in sys which allows us to access the tool box
from PySide6.QtWidgets import QApplication, QWidget # I have asked  Pyside6 library to bring in the QApplication and QWidget classes from the QtWidgets module. This will allow us to create a GUI application and a window for our paint program.
from PySide6.QtGui import QImage, QPainter #QImage is a class that allows us to create and manipulate images in our paint program. QPainter is a class that allows us to draw on the canvas in our paint program.
from PySide6.QtCore import Qt #bag of useful constants: color names, key codes, and so on. We need it for the color white.
from PySide6.QtGui import QImage, QPainter, QPen, QColor
#Qpen is a class that describes how to draw: color, thickness, line style
#QColor is a class that describes a color in terms of its red, green, blue, and alpha (transparency) components. We will use it to set the color of the pen that we will use to draw on the canvas.
from PySide6.QtCore import Qt, QPoint
#Qpoint is a class that describes a point in 2D space. like x and y axis


#Right now the QWidget is just a blank window. We will need to add a canvas to the window so we cann add to it 

# Here I have created a class called Canvas that inherits from QWidget. 
# I have also created a superclass that will allow me to access the methods and properties of Qwidget. So I will be able to use the methods and properties of QWidget in my Canvas class and be able to add my own methods and properties to the canvas class. 

class Canvas(QWidget): #class Canvas that inherits from QWidget. blueprint named Canvas, based on QWidget 
    def __init__(self): #We made a constructor method that will be called when we create an instance of the Canvas class by defining the __init__ method. This method will be called when we are creating an instance of the Canvas class. Every method in a class receives self as its first ingredient

        super().__init__() #Before we can add our own methods and properties to the Canvas class, we need to call the constructor of the superclass (QWidget) using super().__init__(). This will initialize the QWidget part of our Canvas class and allow us to use its methods and properties.
        #Skipping this line means the widget machinery never gets initialized, and things break in confusing ways
        self.image = QImage(800, 600, QImage.Format_RGB32)
        self.image.fill(Qt.white) #changes the color of the canvas depending what we assigne it to.

        self.drawing = False #this is a boolean variable that will be used to determine if the user is currently drawing on the canvas or not. It will be set to True when the user presses the left mouse button and set to False when the user releases the left mouse button.
        self.last_point = QPoint() # buiilds an empty postion that will be use as placeholder for the last point where the user drew on the canavas. it will be updated every time the user draws on the canvas. 
        self.pen_color = QColor("black") #sets the color of the pen 
        self.pen_width = 3 #size of the pen 


    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawImage(0, 0, self.image)
        painter.end()

# I have created a method by using a if statement to check if the left mouse button is pressed. 
#If its true then it goes head and sets the drawing variable to true and sets the last_point variable to the position of the mouse when the left button is pressed.
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton: #
            self.drawing = True
            self.last_point = event.position().toPoint()
            #this command asks for the position of the mouse when the left button is pressed and converts it to a QPoint object. 
            # This will be used as the starting point for drawing on the canvas.

# this method is called after the mousePressEvent method is active and the use is moving the mouse while holding down the left mouse
    def mouseMoveEvent(self,event):
        if self.drawing: # bail out unless the user is mid drag
            current_point = event.position().toPoint() # this will get the current position of the mouse and convert it to a QPoint object. This will be used as the ending point for drawing on the canvas.
            # draw a tiny line from where we were to where we are now
            painter = QPainter(self.image)#
            pen = QPen(self.pen_color, self.pen_width, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
            painter.setPen(pen)
            painter.drawLine(self.last_point, current_point)
            painter.end()
            self.last_point = current_point
            self.update() 
    

        
#getting the winow ready to display

app = QApplication(sys.argv) #creates an application engine where app is the name of the variable that will hold the application engine.
window = Canvas() #creates one blank widget — the parentheses mean "make one now." 
window.setWindowTitle("My Paint") # sets the title of the window to "My Paint" (The dot means "hey window, do this action)
window.resize(800,600) # this sets the size of our window size
window.show() # this will display the window on the screen

sys.exit(app.exec()) # this will keep the application running in a loop until the use closes the window

