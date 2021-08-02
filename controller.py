from PyQt6 import QtGui, QtCore
from functools import partial
from worker import Worker


class PathfinderController(QtCore.QObject):
    def __init__(self, view, model):
        super().__init__()
        self._view = view
        self._model = model
        self.algorithm = 'dijkstra'
        # Connect signals and slots
        self._connectSignals()

    def _connectSignals(self):
        # connecting options buttons
        self._view.startPositionButton.clicked.connect(self.setStartPosition)
        self._view.endPositionButton.clicked.connect(self.setEndPosition)
        self._view.wallButton.clicked.connect(self.setWall)
        self._view.runCodeButton.clicked.connect(self.runCode)
        self._model.colorChange.connect(self.changeSquareColor)

        # connecting squares
        for row in self._view.pathList:
            for square in row:
                square.clicked.connect(self.squareClicked)
                self._model.clearSquares.connect(square.changeToWhite)

    def squareClicked(self):
        if self._view.scopeToClear:
            worker = Worker(self._model.clearScope)
            self._view.scopeToClear = False
            self._view.threadPool.start(worker)
        sender = self._view.sender()
        senderName = sender.objectName()
        i, j = senderName.split('-')[1], senderName.split('-')[2]
        if self._view.actualIcon == 'start.png':
            if i == self._view.endI and j == self._view.endJ or sender.styleSheet() == self._view.blackSquareStr:
                return
            self._view.startI = i
            self._view.startJ = j
            usedIcon = QtGui.QIcon(self._view.actualIcon)
            self.clearPreviousStartPosition()
            sender.setIcon(usedIcon)
            sender.setAccessibleName("start")
        elif self._view.actualIcon == "end.png":
            if i == self._view.startI and j == self._view.startJ or sender.styleSheet() == self._view.blackSquareStr:
                return
            self._view.endI = i
            self._view.endJ = j
            usedIcon = QtGui.QIcon(self._view.actualIcon)
            self.clearPreviousEndPosition()
            sender.setIcon(usedIcon)
            sender.setAccessibleName("end")
        else:
            if i == self._view.startI and j == self._view.startJ or i == self._view.endI and j == self._view.endJ:
                return
            elif sender.styleSheet() != self._view.blackSquareStr:
                sender.setStyleSheet(self._view.blackSquareStr)
            else:
                sender.setStyleSheet(self._view.whiteSquareStr)

    def clearPreviousStartPosition(self):
        for row in self._view.pathList:
            for square in row:
                if square.accessibleName() == "start":
                    square.setIcon(QtGui.QIcon(''))
                    square.setAccessibleName('')
                    return

    def clearPreviousEndPosition(self):
        for row in self._view.pathList:
            for square in row:
                if square.accessibleName() == 'end':
                    square.setIcon(QtGui.QIcon(''))
                    square.setAccessibleName('')
                    return

    def changeSquareColor(self, i, j, color):
        self._view.pathList[i][j].setStyleSheet(color)

    def setStartPosition(self):
        if self._view.endPositionButton.isEnabled():
            self._view.wallButton.setEnabled(True)
        else:
            self._view.endPositionButton.setEnabled(True)
        self._view.startPositionButton.setDisabled(True)
        self._view.actualIcon = "start.png"

    def setEndPosition(self):
        if self._view.startPositionButton.isEnabled():
            self._view.wallButton.setEnabled(True)
        else:
            self._view.startPositionButton.setEnabled(True)
        self._view.endPositionButton.setDisabled(True)
        self._view.actualIcon = "end.png"

    def setWall(self):
        if self._view.startPositionButton.isEnabled():
            self._view.endPositionButton.setEnabled(True)
        else:
            self._view.startPositionButton.setEnabled(True)
        self._view.wallButton.setDisabled(True)
        self._view.actualIcon = ''

    def runCode(self):
        # clear scope before running algorithm
        if self._view.scopeToClear:
            worker = Worker(self._model.clearScope)
            self._view.scopeToClear = False
            worker.signals.finished.connect(self.runCode)
            self._view.threadPool.start(worker)
        else:
            # choose algorithm and pass it to worker class
            if self.algorithm == 'dijkstra':
                worker = Worker(self._model.dijkstraShortestPath,
                                (self._view.startI, self._view.startJ),
                                (self._view.endI, self._view.endJ),
                                self._view.pathList)
            # buttons resets
            self._view.runCodeButton.setDisabled(True)
            self._view.startPositionButton.setDisabled(True)
            self._view.endPositionButton.setDisabled(True)
            self._view.wallButton.setDisabled(True)
            worker.signals.finished.connect(partial(self._view.runCodeButton.setEnabled, True))
            if self._view.actualIcon == 'start.png':
                worker.signals.finished.connect(partial(self._view.endPositionButton.setEnabled, True))
                worker.signals.finished.connect(partial(self._view.wallButton.setEnabled, True))
            elif self._view.actualIcon == 'end.png':
                worker.signals.finished.connect(partial(self._view.startPositionButton.setEnabled, True))
                worker.signals.finished.connect(partial(self._view.wallButton.setEnabled, True))
            else:
                worker.signals.finished.connect(partial(self._view.startPositionButton.setEnabled, True))
                worker.signals.finished.connect(partial(self._view.endPositionButton.setEnabled, True))
            self._view.scopeToClear = True
            self._view.threadPool.start(worker)