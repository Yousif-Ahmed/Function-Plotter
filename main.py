from Validate import Validate
import sys
import matplotlib
import numpy as np
import re

from PySide2.QtWidgets import QLabel, QLineEdit, QMainWindow, QMessageBox, QPushButton, QVBoxLayout, QWidget, QApplication
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class Function_plotter(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(Function_plotter, self).__init__(*args, **kwargs)
        #Setting window paremeter
        self.setWindowTitle("Function Plotter")
        self.errorMessage = None
        self.setup()
        
       

    def setup(self):
        """"
        setup all widgets in the window 

        """
        self.CreatingMplcanavs__()
        self.CreatingInputfunc__()
        self.CreatingInputMax__()
        self.CreatingButton__()
        self.CreatingInputMin__()
        self.Creatingverticallayout__()

    def CreatingMplcanavs__(self):
        """"
        Creating canavas for ploting our function

        """
        self.sc = MplCanvas(self, width=5, height=4, dpi=100)

        # Create toolbar, passing canvas as first parament, parent (self, the MainWindow) as second.
        self.toolbar = NavigationToolbar(self.sc, self)


    def CreatingButton__(self):

        self.plot_btn =QPushButton("Plot",self) #setting button text
        self.plot_btn.clicked.connect(self.__Onclick__) #setting

    def CreatingInputfunc__(self):
        self.func_input = QLineEdit(self)
        self.func_label = QLabel(self)
        self.func_label.setText("f(x)") 
           
    
    def CreatingInputMax__(self):
        self.Max_input = QLineEdit(self) 
        self.Max_label = QLabel(self)
        self.Max_label.setText("Max value of x")

    
    def CreatingInputMin__ (self):   
        self.Min_input = QLineEdit(self)
        self.Min_label = QLabel(self)
        self.Min_label.setText("Min value of x")

    def Creatingverticallayout__ (self):
        
        layout = QVBoxLayout()  #working with vertical layout box 
        
        #adding toolbar and Mplcanavas widegts
        layout.addWidget(self.toolbar)
        layout.addWidget(self.sc)

        #adding function label and function input widgets
        layout.addWidget(self.func_label)
        layout.addWidget(self.func_input)

        #adding Maximum value label and Maximum value input widgets
        layout.addWidget(self.Max_label)
        layout.addWidget(self.Max_input)

        #adding function label and function input widgets
        layout.addWidget(self.Min_label)
        layout.addWidget(self.Min_input)

        layout.addWidget(self.plot_btn)
        
        # Create a placeholder widget to hold our toolbar and canvas.
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    
    def displayErrorMessage(self , err):
        message = QMessageBox.warning(self, 'Error Message', 'Please, '+ err , 
        QMessageBox.Ok , QMessageBox.Ok)
        

    def Plotfunc__(self , fx:str , max , min ):
         
         x = np.linspace(float(min) , float(max) ) #array of x of range from min to max
         fx = fx.replace("^" ,"**").replace(" ","").replace("sin","np.sin").replace("cos","np.cos").replace("tan" ,"np.tan").replace("e^","np.exp")
         self.sc.axes.clear()
         self.sc.axes.plot(x, eval(fx))
         self.sc.draw()

    

    def __Onclick__(self):

        # clear 
        self.sc.axes.clear()

        # chicking input validation 
        fx = self.func_input.text().lower()
        min = self.Min_input.text()
        max = self.Max_input.text()
        
        try:
            validation_param =Validate(fx , min , max)
            self.Plotfunc__(fx , max , min)
        except ValueError as error:
            self.errorMessage= error.args[0] 
            self.displayErrorMessage(self.errorMessage)
            self.errorMessage =None
            
 
           


if __name__ == '__main__':
    app = QApplication(sys.argv)
    plotter = Function_plotter()
    plotter.show()
    sys.exit(app.exec_())    



