from PyQt6 import QtCore
import time


class PathFinderModel(QtCore.QObject):
    colorChange = QtCore.pyqtSignal(int, int, str)
    clearSquares = QtCore.pyqtSignal(bool)
    resetPoints = QtCore.pyqtSignal()

    def __init__(self):
        super(PathFinderModel, self).__init__()
        self.clearSquareStr = 'background-color:white;'
        self.checkedStr = 'background-color:purple;'
        self.pathStr = 'background-color:yellow;'

    def clearScope(self):
        self.clearSquares.emit(True)

    def clearAll(self):
        self.clearSquares.emit(False)
        self.resetPoints.emit()

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

    def aStar(self, start, end, scope):
        parents = {}
        toBeChecked = [(int(start[0]), int(start[1]))]
        alreadyChecked = []
        shortestPath = []
        while True:
            if not toBeChecked:
                return
            current = self.findLowestFCost(toBeChecked, start, end)
            toBeChecked.remove(current)
            alreadyChecked.append(current)
            self.colorChange.emit(current[0], current[1], self.checkedStr)

            if current == (int(end[0]), int(end[1])):
                lastI, lastJ = current[0], current[1]
                shortestPath.append((lastI, lastJ))
                while (lastI, lastJ) != (int(start[0]), int(start[1])):
                    lastI, lastJ = parents[lastI, lastJ]
                    shortestPath.append((lastI, lastJ))
                for position in reversed(shortestPath):
                    self.colorChange.emit(position[0], position[1], self.pathStr)
                    time.sleep(0.01)
                return

            possibleNeighbours = [
                (current[0], current[1] + 1), (current[0], current[1] - 1),
                (current[0] - 1, current[1]), (current[0] + 1, current[1])
            ]
            for neighbour in possibleNeighbours:
                if 0 > neighbour[0] or neighbour[0] > 24 or 0 > neighbour[1] or neighbour[1] > 49:
                    continue
                if scope[neighbour[0]][neighbour[1]].styleSheet() == 'background-color:black;' or \
                        neighbour in alreadyChecked:
                    continue
                if neighbour not in toBeChecked and 0 <= neighbour[0] <= 24 and 0 <= neighbour[1] <= 49:
                    parents[neighbour] = current
                    toBeChecked.append(neighbour)
            time.sleep(0.01)


    def findGCost(self, checked, start):
        return abs(checked[0] - int(start[0])) + abs(checked[1] - int(start[1]))

    def findHCost(self, checked, end):
        return abs(checked[0] - int(end[0])) + abs(checked[1] - int(end[1]))

    def findLowestFCost(self, positions, start, end):
        i = 0
        bestK = 0
        for position in positions:
            if i == 0:
                min = self.findGCost(position, start) + self.findHCost(position, end)
                bestK = position
                i += 1
            else:
                value = self.findGCost(position, start) + self.findHCost(position, end)
                if value < min:
                    min = value
                    bestK = position
        return bestK