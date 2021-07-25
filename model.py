from PyQt6 import QtCore
import time


class PathFinderModel(QtCore.QObject):
    colorChange = QtCore.pyqtSignal(int, int, str)

    def __init__(self):
        super(PathFinderModel, self).__init__()
        self.clearSquareStr = 'background-color:white;'
        self.checkedStr = 'background-color:purple;'
        self.pathStr = 'background-color:yellow;'

    def clearScope(self, scope):
        for row in scope:
            for square in row:
                if square.styleSheet() != 'background-color:black;':
                    i, j = int(square.objectName().split('-')[1]), int(square.objectName().split('-')[2])
                    self.colorChange.emit(i, j, self.clearSquareStr)

    def dijkstraShortestPath(self, start, end, scope):
        parentDict = {}
        shortestPath = []
        alreadyChecked = {}
        for row in scope:
            for square in row:
                i, j = int(square.objectName().split('-')[1]), int(square.objectName().split('-')[2])
                alreadyChecked[(i, j)] = False
        alreadyChecked[(int(start[0]), int(start[1]))] = True
        recentlyChecked = [(int(start[0]), int(start[1]))]
        self.colorChange.emit(int(start[0]), int(start[1]), self.checkedStr)
        while True:
            toBeChecked = []
            if not recentlyChecked:
                return
            for position in recentlyChecked:
                edges = [
                    (int(position[0]), int(position[1]) - 1), (int(position[0]), int(position[1]) + 1),
                    (int(position[0]) + 1, int(position[1])), (int(position[0]) - 1, int(position[1]))
                ]
                for square in edges:
                    if 0 <= square[0] <= 24 and 0 <= square[1] <= 49:
                        if not alreadyChecked[(square[0], square[1])] \
                                and scope[square[0]][square[1]].styleSheet() != "background-color:black;":
                            toBeChecked.append((square[0], square[1]))
                            parentDict[(square[0], square[1])] = (position[0], position[1])
                            alreadyChecked[(square[0], square[1])] = True

                if position[0] == int(end[0]) and position[1] == int(end[1]):
                    lastI, lastJ = position[0], position[1]
                    shortestPath.append((lastI, lastJ))
                    while (lastI, lastJ) != (int(start[0]), int(start[1])):
                        lastI, lastJ = parentDict[(lastI, lastJ)]
                        shortestPath.append((lastI, lastJ))
                    for square in reversed(shortestPath):
                        time.sleep(0.01)
                        self.colorChange.emit(square[0], square[1], self.pathStr)
                    return
            time.sleep(0.05)
            recentlyChecked = []
            for square in toBeChecked:
                recentlyChecked.append(square)
                self.colorChange.emit(square[0], square[1], self.checkedStr)