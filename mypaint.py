import sys # this will bring in python's built-in sys which allows us to access the tool box
from PySide6.QtWidgets import QApplication, QWidget # I have asked  Pyside6 library to bring in the QApplication and QWidget classes from the QtWidgets module. This will allow us to create a GUI application and a window for our paint program.

#getting the winow ready to display
app = QApplication(sys.argv) #creates an application engine where app is the name of the variable that will hold the application engine.
window = QWidget() #creates one blank widget — the parentheses mean "make one now." 
window.setWindowTitle("My Paint") # sets the title of the window to "My Paint" (The dot means "hey window, do this action)
window.resize(800,600) # this sets the size of our window size
window.show() # this will display the window on the screen
sys.exit(app.exec()) # this will keep the application running in a loop until the use closes the window