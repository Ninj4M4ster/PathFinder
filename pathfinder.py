from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtCore import Qt
import sys

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        # main window properties
        self.setGeometry(100, 100, 1500, 800)
        self.setMinimumSize(1500, 800)
        self.setWindowTitle("Path Finding Visualisation")

        # main window layout
        self.container = QtWidgets.QVBoxLayout(self)

        # title label
        self.titleLabel = QtWidgets.QLabel(self)
        self.titleLabel.setText("Welcome to path finding visualisation")
        self.titleLabel.setObjectName("titleLabel")
        self.titleLabel.setMinimumSize(700, 70)
        self.titleLabel.setMaximumSize(900, 70)
        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # adding title label to main window's layout
        self.container.addWidget(self.titleLabel, alignment=Qt.AlignmentFlag.AlignJustify)

        # description label
        self.descriptionLabel = QtWidgets.QLabel(self)
        self.descriptionLabel.setText("Pick an algorithm from all available. \nSet start and end points, create\
obstacles if you need them and run the code!")
        self.descriptionLabel.setMinimumSize(500, 50)
        self.descriptionLabel.setMaximumSize(500, 50)
        self.descriptionLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # adding description label to main window's layout
        self.container.addWidget(self.descriptionLabel, alignment=Qt.AlignmentFlag.AlignJustify)

        # label for algorithms buttons
        self.algorithms = QtWidgets.QLabel(self)
        self.algorithms.setMinimumSize(1000, 50)
        self.algorithms.setMaximumSize(1200, 50)

        # adding algorithms label to main window's layout
        self.container.addWidget(self.algorithms, alignment=Qt.AlignmentFlag.AlignJustify)
        # algorithms grid layout
        self.algorithmButtonsLayout = QtWidgets.QGridLayout(self.algorithms)

        # Shortest path algorithm's button
        self.firstAlgorithm = QtWidgets.QPushButton(self.algorithms)
        self.firstAlgorithm.setText("Shortest Path")
        self.algorithmButtonsLayout.addWidget(self.firstAlgorithm, 0, 0)
        # A* algorithm's button
        self.secondAlgorithm = QtWidgets.QPushButton(self.algorithms)
        self.secondAlgorithm.setText("A*")
        self.algorithmButtonsLayout.addWidget(self.secondAlgorithm, 0, 1)
        # Yen's k-Shortest Paths algorithm's button
        self.thirdAlgorithm = QtWidgets.QPushButton(self.algorithms)
        self.thirdAlgorithm.setText("Yen’s k-Shortest Paths")
        self.algorithmButtonsLayout.addWidget(self.thirdAlgorithm, 0, 2)
        # All-Pairs Shortest Path algorithm's button
        self.fourthAlgorithm = QtWidgets.QPushButton(self.algorithms)
        self.fourthAlgorithm.setText("All-Pairs Shortest Path")
        self.algorithmButtonsLayout.addWidget(self.fourthAlgorithm, 0, 3)
        # Single Source Shortest Path algorithm's button
        self.fifthAlgorithm = QtWidgets.QPushButton(self.algorithms)
        self.fifthAlgorithm.setText("Single Source Shortest Path")
        self.algorithmButtonsLayout.addWidget(self.fifthAlgorithm, 0, 4)
        # Minimum Spanning Tree algorithm's button
        self.sixthAlgorithm = QtWidgets.QPushButton(self.algorithms)
        self.sixthAlgorithm.setText("Minimum Spanning Tree")
        self.algorithmButtonsLayout.addWidget(self.sixthAlgorithm, 0, 5)
        # Random Walk algorithm's button
        self.seventhAlgorithm = QtWidgets.QPushButton(self.algorithms)
        self.seventhAlgorithm.setText("Random Walk")
        self.algorithmButtonsLayout.addWidget(self.seventhAlgorithm, 0, 6)

        # layout for main content
        self.centralLayout = QtWidgets.QHBoxLayout(self)

        # field for path finding
        self.centralWidget = QtWidgets.QLabel(self)
        self.centralWidget.setObjectName("central")
        self.centralWidget.setMinimumSize(1055, 530)
        self.centralWidget.setMaximumSize(1055, 530)
        # adding field to main content's layout
        self.centralLayout.addWidget(self.centralWidget)
        # label for options used with path finding
        self.optionsLabel = QtWidgets.QLabel(self)
        self.optionsLabel.setFixedSize(300, 530)
        # layout for options
        self.optionsLayout = QtWidgets.QVBoxLayout(self.optionsLabel)

        # buttons' icons QSize instance
        buttonIconSize = QtCore.QSize(32, 32)
        # squares' icons QSize instance
        squareIconSize = QtCore.QSize(16, 16)

        # properties for path finding algotihm and program
        self.onlyOnePossible = True
        self.actualIcon = "start.png"
        self.startI = -1
        self.endI = -1
        self.startJ = -1
        self.endJ = -1
        # start position button
        self.startPositionButton = QtWidgets.QPushButton(self)
        self.startPositionButton.setFixedSize(200, 40)
        self.startPositionButton.setText("Start position")
        startPositionIcon = QtGui.QIcon("start.png")
        self.startPositionButton.setIcon(startPositionIcon)
        self.startPositionButton.setIconSize(buttonIconSize)
        self.startPositionButton.clicked.connect(self.setStartPosition)
        self.startPositionButton.setDisabled(True)
        self.optionsLayout.addWidget(self.startPositionButton)
        # end position button
        self.endPositionButton = QtWidgets.QPushButton(self)
        self.endPositionButton.setFixedSize(200, 40)
        self.endPositionButton.setText("End position")
        endPositionIcon = QtGui.QIcon("end.png")
        self.endPositionButton.setIcon(endPositionIcon)
        self.endPositionButton.setIconSize(buttonIconSize)
        self.endPositionButton.clicked.connect(self.setEndPosition)
        self.optionsLayout.addWidget(self.endPositionButton)
        # wall button
        self.wallButton = QtWidgets.QPushButton(self)
        self.wallButton.setFixedSize(200, 40)
        self.wallButton.setText("Wall")
        self.optionsLayout.addWidget(self.wallButton)
        # code starting button
        self.runCodeButton = QtWidgets.QPushButton(self)
        self.runCodeButton.setFixedSize(200, 40)
        self.runCodeButton.setText("Run code")
        self.optionsLayout.addWidget(self.runCodeButton)

        # add options label to main content's layout
        self.centralLayout.addWidget(self.optionsLabel)
        # add main content's layout to window's layout
        self.container.addLayout(self.centralLayout)

        # squares for field and nested list for all squares
        self.pathList = []
        for i in range(25):
            tmpList = []
            for j in range(50):
                square = QtWidgets.QPushButton(self.centralWidget)
                square.setMinimumSize(20, 20)
                square.setMaximumSize(20, 20)
                square.setObjectName(f"square-{i}-{j}")
                square.setAccessibleName('')
                square.move(j*21 + 3, i*21 + 3)
                square.clicked.connect(self.on_clicked)
                square.setIconSize(squareIconSize)
                tmpList.append(square)
            self.pathList.append(tmpList)

        # stylesheet
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
        """
        self.setStyleSheet(stylesheetstr)

    def on_clicked(self):
        sender = self.sender()
        senderName = sender.objectName()
        i, j = senderName.split('-')[1], senderName.split('-')[2]
        if self.actualIcon == 'start.png':
            self.startI = i
            self.startJ = j
            usedIcon = QtGui.QIcon(self.actualIcon)
            self.clearPreviousStartPosition()
            sender.setIcon(usedIcon)
            sender.setAccessibleName("start")
        elif self.actualIcon == "end.png":
            self.endI = i
            self.endJ = j
            usedIcon = QtGui.QIcon(self.actualIcon)
            self.clearPreviousEndPosition()
            sender.setIcon(usedIcon)
            sender.setAccessibleName("end")


    def clearPreviousStartPosition(self):
        for row in self.pathList:
            for square in row:
                if square.accessibleName() == "start":
                    square.setIcon(QtGui.QIcon(''))
                    square.setAccessibleName('')
                    return

    def clearPreviousEndPosition(self):
        for row in self.pathList:
            for square in row:
                if square.accessibleName() == 'end':
                    square.setIcon(QtGui.QIcon(''))
                    square.setAccessibleName('')
                    return

    def setStartPosition(self):
        if self.endPositionButton.isEnabled():
            self.wallButton.setEnabled(True)
        else:
            self.endPositionButton.setEnabled(True)
        self.startPositionButton.setDisabled(True)
        self.actualIcon = "start.png"
        self.onlyOnePossible = True

    def setEndPosition(self):
        if self.startPositionButton.isEnabled():
            self.wallButton.setEnabled(True)
        else:
            self.startPositionButton.setEnabled(True)
        self.endPositionButton.setDisabled(True)
        self.actualIcon = "end.png"

def main():
    app = QtWidgets.QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    app.exec()

if __name__ == '__main__':
    main()