import sys
from PySide2.QtWidgets import (QLineEdit, QPushButton, QApplication,
    QVBoxLayout, QDialog,QLabel)
from PySide2 import QtCore, QtGui
from Code_files.function_plotter_ import plot

class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        pixmap = QtGui.QPixmap('Code_files/graph.png') ##
        # Create widgets
        self.label=QLabel('Function:')
        self.edit = QLineEdit("5*x^3 + 2*x")          # function of x
        self.label2 = QLabel('Min:')
        self.edit2 = QLineEdit("-10")                 # min
        self.label3 = QLabel('Max:')
        self.edit3 = QLineEdit("10")                  # max
        self.button = QPushButton("Plot Function")
        self.lbl = QLabel(self)
        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.edit)
        layout.addWidget(self.label2)
        layout.addWidget(self.edit2)
        layout.addWidget(self.label3)
        layout.addWidget(self.edit3)
        layout.addWidget(self.button)
        layout.addWidget(self.lbl)
        # Set dialog layout
        self.setLayout(layout)
        # Add button signal to greetings slot
        self.button.clicked.connect(self.plot_function)




        # self.home()

    def home(self):
        self.show()

    # Validating User-inputs
    def validate_input(self,func,min,max):
        l = ' 0123456789+-*/^x'
        # testing the function
        for i in func:
            if i in l:
                pass
            else:
                print(f"{i} can't be in the function, example: 5*x^3 + 2*x")

        # testing min value
        try:
            float(min)
        except:
            print('Min must be an int or float')
        # testing max value
        try:
            float(max)
        except:
            print('Max must be an int or float')

    # Plotting the user-input function
    def plot_function(self):
        f=self.edit.text()
        min=self.edit2.text()
        max=self.edit3.text()
        self.validate_input(f,min,max)
        plot(f,float(min),float(max))

        self.image = QtGui.QImage(
            'F:/courses/Programming/All Python/Projects folder/Function_Plotter/Code_files/graphs/graph.png')
        pixmap = QtGui.QPixmap(self.image)
        self.lbl.setPixmap(pixmap)

def main():
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    form = Form()
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec_())