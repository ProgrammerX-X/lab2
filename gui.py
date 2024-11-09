import sys
from PyQt6.QtWidgets import QMainWindow, QLabel, QApplication, QRadioButton, \
    QPushButton, QButtonGroup, QTextEdit
from PyQt6.QtGui import QFont
import numpy as np
import sympy as sp

from squareMeth import squareMethod
from trapMeth import trapezoidMethod
from mcMeth import monteCarloMethod

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculating methods")
        self.resize(600, 400)
        self.move(350, 160)

        fontIter = QFont("Arial", 10)

        self.label = QLabel("Чисельні методи", self)
        self.label.move(225, 10)
        self.label.setFixedSize(600, 50)

        font = QFont("Arial", 15)
        font.setBold(True)
        self.label.setFont(font)

        self.method = QLabel("Виберіть метод для обробки", self)
        self.method.move(30, 60)
        self.method.setFixedSize(175, 40)

        self.square = QRadioButton("Метод прямокутника", self)
        self.square.move(30, 90)
        self.square.setFixedSize(175, 40)
        self.square.setChecked(True)
        
        self.trapezoid = QRadioButton("Метод трапеції", self)
        self.trapezoid.move(30, 120)
        self.trapezoid.setFixedSize(175, 40)

        self.monteCarlo = QRadioButton("Метод Монте-Карло", self)
        self.monteCarlo.move(30, 150)
        self.monteCarlo.setFixedSize(175, 40)

        self.methodGroup = QButtonGroup(self)
        self.methodGroup.addButton(self.square)
        self.methodGroup.addButton(self.trapezoid)
        self.methodGroup.addButton(self.monteCarlo)

        self.equation = QLabel("Виберіть рівняння", self)
        self.equation.move(410, 60)
        self.equation.setFixedSize(130, 40)
        self.equation.setFont(fontIter)

        self.firstEq = QRadioButton("4*sqrt(0.5*x+1)", self)
        self.firstEq.move(410, 90)
        self.firstEq.setFixedSize(130, 40)
        self.firstEq.setChecked(True)

        self.secondEq = QRadioButton("log(x**2+3)**2/4", self)
        self.secondEq.move(410, 120)
        self.secondEq.setFixedSize(130, 40)

        self.thirdEq = QRadioButton("log(x+np.sqrt(x**2+6)", self)
        self.thirdEq.move(410, 150)
        self.thirdEq.setFixedSize(150, 40)

        self.eqGroup = QButtonGroup(self)
        self.eqGroup.addButton(self.firstEq)
        self.eqGroup.addButton(self.secondEq)
        self.eqGroup.addButton(self.thirdEq)

        self.calculating = QPushButton("Розрахувати", self)
        self.calculating.move(240, 300)
        self.calculating.setFixedSize(130, 40)
        self.calculating.setFont(fontIter)
        self.calculating.clicked.connect(self.isCheckFunction)

        self.method.setFont(fontIter)
        
        self.title = QLabel("Виберіть межі та кількість розбиттів", self)
        self.title.move(200, 200)
        self.title.setFixedSize(220, 40)
        self.title.setFont(fontIter)

        self.limitA = QTextEdit(self)
        self.limitA.move(130, 250)
        self.limitA.setFixedSize(100, 40)
        self.limitA.setPlaceholderText("Межа А: 1.2")
        self.limitA.setPlainText(str(1.2))

        self.limitB = QTextEdit(self)
        self.limitB.move(250, 250)
        self.limitB.setFixedSize(100, 40)
        self.limitB.setPlaceholderText("Межа В: 2.0")
        self.limitB.setPlainText(str(2.0))

        self.n = QTextEdit(self)
        self.n.move(370, 250)
        self.n.setFixedSize(100, 40)
        self.n.setPlaceholderText("К-сть розбиттів n: 10")
        self.n.setPlainText(str(10))

    def f1(self, x):
        return 4*np.sqrt(0.5*x+1)

    def f2(self, x):
        return (np.log(x**2+3)**2)/4
        
    def f3(self, x):
        return np.log(x+np.sqrt(x**2+6))

    def isCheckFunction(self):
        try:
            a = float(self.limitA.toPlainText())
            b = float(self.limitB.toPlainText())
            n = float(self.n.toPlainText())
        except ValueError:
            print("Invalid input values. Please enter numeric values for limits and epsilon.")
            return

        if self.square.isChecked() and self.firstEq.isChecked():
            squareMethod(a, b, n, self.f1)
        elif self.square.isChecked() and self.secondEq.isChecked():
            squareMethod(a, b, n, self.f2)
        elif self.square.isChecked() and self.thirdEq.isChecked():
            squareMethod(a, b, n, self.f3)
        elif self.trapezoid.isChecked() and self.firstEq.isChecked():
            trapezoidMethod(a, b, n, self.f1)
        elif self.trapezoid.isChecked() and self.secondEq.isChecked():
            trapezoidMethod(a, b, n, self.f2)
        elif self.trapezoid.isChecked() and self.thirdEq.isChecked():
            trapezoidMethod(a, b, n, self.f3)
        elif self.monteCarlo.isChecked() and self.firstEq.isChecked():
            monteCarloMethod(a, b, int(n), self.f1)
        elif self.monteCarlo.isChecked() and self.secondEq.isChecked():
            monteCarloMethod(a, b, int(n), self.f2)
        else:
            monteCarloMethod(a, b, int(n), self.f3)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
