from PyQt5 import QtWidgets
import sys
from temperature import Ui_MainWindow


class myApp(QtWidgets.QMainWindow):

    def __init__(self):
        super(myApp,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.Fahrenbutton.clicked.connect(self.FahrenToCalc)
        self.ui.Celcbutton.clicked.connect(self.CalcToCFahr)



    def FahrenToCalc(self):
        Fahrenheit = float(self.ui.lineEdit.text())
        FahrtoCalc = ((Fahrenheit -32 ) * 5) / 9
        return self.ui.result1.setText(f'{Fahrenheit} Fahrenheit : {FahrtoCalc}  Celcius ')
    

    def CalcToCFahr(self):
        Celcius = float(self.ui.lineEdit_2.text())
        CelctoFahr = ((Celcius*9) / 5) + 32
        return self.ui.result2.setText(f'{Celcius} Celcius : {CelctoFahr} Fahrenheit')






def app():
    app = QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec())


app()