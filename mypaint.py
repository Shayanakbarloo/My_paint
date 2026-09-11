import sys # this will bring in python's built-in sys which allows us to access the tool box
from PySide6.QtWidgets import QApplication, QWidget # I have asked  Pyside6 library to bring in the QApplication and QWidget classes from the QtWidgets module. This will allow us to create a GUI application and a window for our paint program.
from PySide6.QtGui import QImage, QPainter #QImage is a class that allows us to create and manipulate images in our paint program. QPainter is a class that allows us to draw on the canvas in our paint program.
from PySide6.QtCore import Qt #bag of useful constants: color names, key codes, and so on. We need it for the color white.
from PySide6.QtGui import QImage, QPainter, QPen, QColor
from PySide6.QtCore import Qt, QPoint

#Right now the QWidget is just a blank window. We will need to add a canvas to the window so we cann add to it 

# Here I have created a class called Canvas that inherits from QWidget. 
# I have also created a superclass that will allow me to access the methods and properties of Qwidget. So I will be able to use the methods and properties of QWidget in my Canvas class and be able to add my own methods and properties to the canvas class. 

class Canvas(QWidget): #class Canvas that inherits from QWidget. blueprint named Canvas, based on QWidget 
    def __init__(self): #We made a constructor method that will be called when we create an instance of the Canvas class by defining the __init__ method. This method will be called when we are creating an instance of the Canvas class. Every method in a class receives self as its first ingredient
        super().__init__() #Before we can add our own methods and properties to the Canvas class, we need to call the constructor of the superclass (QWidget) using super().__init__(). This will initialize the QWidget part of our Canvas class and allow us to use its methods and properties.
        #Skipping this line means the widget machinery never gets initialized, and things break in confusing ways
        self.image = QImage(800, 600, QImage.Format_RGB32)
        self.image.fill(Qt.white)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawImage(0, 0, self.image)
        painter.end()
        
#getting the winow ready to display

app = QApplication(sys.argv) #creates an application engine where app is the name of the variable that will hold the application engine.
window = Canvas() #creates one blank widget — the parentheses mean "make one now." 
window.setWindowTitle("My Paint") # sets the title of the window to "My Paint" (The dot means "hey window, do this action)
window.resize(800,600) # this sets the size of our window size
window.show() # this will display the window on the screen

sys.exit(app.exec()) # this will keep the application running in a loop until the use closes the window

