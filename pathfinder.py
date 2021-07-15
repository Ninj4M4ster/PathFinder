from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtCore import Qt
import sys

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 1500, 800)
        self.setMinimumSize(1500, 800)
        self.setWindowTitle("Path Finding Visualisation")

        self.containter = QtWidgets.QVBoxLayout(self)

        self.titleLabel = QtWidgets.QLabel(self)
        self.titleLabel.setText("Welcome to path finding visualisation")
        self.titleLabel.setObjectName("titleLabel")
        self.containter.addWidget(self.titleLabel, alignment=Qt.AlignmentFlag.AlignJustify)
        self.titleLabel.setMinimumSize(700, 70)
        self.titleLabel.setMaximumSize(900, 70)
        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.descriptionLabelOne = QtWidgets.QLabel(self)
        self.descriptionLabelOne.setText("Pick an algorithm from all available. \nSet start and end points, create\
obstacles if you need them and run the code!")
        self.containter.addWidget(self.descriptionLabelOne, alignment=Qt.AlignmentFlag.AlignJustify)
        self.descriptionLabelOne.setMinimumSize(500, 50)
        self.descriptionLabelOne.setMaximumSize(500, 50)
        self.descriptionLabelOne.setAlignment(Qt.AlignmentFlag.AlignCenter)


        self.algorithms = QtWidgets.QLabel(self)
        self.containter.addWidget(self.algorithms, alignment=Qt.AlignmentFlag.AlignJustify)
        self.algorithms.setMinimumSize(1000, 50)
        self.algorithms.setMaximumSize(1200, 50)

        self.algorithmButtonsLayout = QtWidgets.QGridLayout(self.algorithms)

        self.firstAlgorithm = QtWidgets.QPushButton(self.algorithms)
        self.firstAlgorithm.setText("Shortest Path")
        self.algorithmButtonsLayout.addWidget(self.firstAlgorithm, 0, 0)

        self.secondAlgorithm = QtWidgets.QPushButton(self.algorithms)
        self.secondAlgorithm.setText("A*")
        self.algorithmButtonsLayout.addWidget(self.secondAlgorithm, 0, 1)

        self.thirdAlgorithm = QtWidgets.QPushButton(self.algorithms)
        self.thirdAlgorithm.setText("Yen’s k-Shortest Paths")
        self.algorithmButtonsLayout.addWidget(self.thirdAlgorithm, 0, 2)

        self.fourthAlgorithm = QtWidgets.QPushButton(self.algorithms)
        self.fourthAlgorithm.setText("All-Pairs Shortest Path")
        self.algorithmButtonsLayout.addWidget(self.fourthAlgorithm, 0, 3)

        self.fifthAlgorithm = QtWidgets.QPushButton(self.algorithms)
        self.fifthAlgorithm.setText("Single Source Shortest Path")
        self.algorithmButtonsLayout.addWidget(self.fifthAlgorithm, 0, 4)

        self.sixthAlgorithm = QtWidgets.QPushButton(self.algorithms)
        self.sixthAlgorithm.setText("Minimum Spanning Tree")
        self.algorithmButtonsLayout.addWidget(self.sixthAlgorithm, 0, 5)

        self.seventhAlgorithm = QtWidgets.QPushButton(self.algorithms)
        self.seventhAlgorithm.setText("Random Walk")
        self.algorithmButtonsLayout.addWidget(self.seventhAlgorithm, 0, 6)

        self.centralWidget = QtWidgets.QLabel(self)
        self.centralWidget.setObjectName("central")
        self.containter.addWidget(self.centralWidget, alignment=Qt.AlignmentFlag.AlignJustify)
        self.centralWidget.setMinimumSize(1055, 530)
        self.centralWidget.setMaximumSize(1055, 530)

        self.pathList = []
        for i in range(25):
            tmpList = []
            for j in range(50):
                square = QtWidgets.QPushButton(self.centralWidget)
                square.setMinimumSize(20, 20)
                square.setMaximumSize(20, 20)
                square.setObjectName(f"square {i} {j}")
                square.move(j*21 + 3, i*21 + 3)
                square.clicked.connect(self.on_clicked)
                tmpList.append(square)
            self.pathList.append(tmpList)




        stylesheetstr = """
            QLabel{
                background-color: red;
            }
            #titleLabel{
                position:relative;
                right:100px;
                font-size:40px;
            }
            #central{
                background-color:grey;
                border:2px solid black;
                border-radius:5px;
            }
            QLabel#central QPushButton{
                background-color:white;
                width:10px;
                height:20px;
                transition: 0.5s;
                border: 1px solid grey;
                border-radius:2px;
                widget-animation-duration: 100;
            }
            QLabel#central QPushButton:hover{
                background-color:black;  
            }
        """
        self.setStyleSheet(stylesheetstr)

    def on_clicked(self):
        sender = self.sender()
        senderName = sender.objectName()
        i, j = senderName.split()[1], senderName.split()[2]
        print(f"position: {i}, {j}")


def main():
    app = QtWidgets.QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    app.exec()

if __name__ == '__main__':
    main()