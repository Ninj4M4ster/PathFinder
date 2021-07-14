from PyQt6 import QtWidgets, QtCore, QtGui
import sys

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 1500, 800)
        self.setWindowTitle("Path Finding Visualisation")

        self.titleLabel = QtWidgets.QLabel(self)
        self.titleLabel.setText("Welcome to path finding visualisation")
        self.titleLabel.setObjectName("titleLabel")

        self.descriptionLabelOne = QtWidgets.QLabel(self)
        self.descriptionLabelOne.setText("Pick an algorithm from all available.")
        self.descriptionLabelOne.move(0, 50)

        self.descriptionLabelTwo = QtWidgets.QLabel(self)
        self.descriptionLabelTwo.setText("Set start and end points, create obstacles if you need them and run the code!")
        self.descriptionLabelTwo.move(0, 65)


        self.algorithms = QtWidgets.QLabel(self)
        self.algorithms.setGeometry(0, 80, 1000, 50)

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
        self.centralWidget.setGeometry(0, 130, 1055, 530)
        self.centralWidget.setObjectName("central")

        for i in range(50):
            for j in range(25):
                square = QtWidgets.QPushButton(self.centralWidget)
                square.setMinimumSize(20, 20)
                square.setMaximumSize(20, 20)
                square.setObjectName(f"square {i} {j}")
                square.move(i*21 + 3, j*21 + 3)
                square.clicked.connect(self.on_clicked)




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
            }
            QLabel#central QPushButton{
                background-color:black;
                width:10px;
                height:20px;
                transition: 0.5s;
            }
            QLabel#central QPushButton:hover{
                background-color:white;
                
            }
        """
        self.setStyleSheet(stylesheetstr)

    def on_clicked(self):
        sender = self.sender()
        senderName = sender.objectName()
        print(senderName)


def main():
    app = QtWidgets.QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    app.exec()

if __name__ == '__main__':
    main()