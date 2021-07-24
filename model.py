import math
import time


class PathFinderModel:

    def __init__(self):
        self.beforeCheckStr = 'background-color:orange;'
        self.checkedStr = 'background-color:purple;'
        self.pathStr = 'background-color:yellow;'

    def dijkstraShortestPath(self, start, end, scope):
        parentDict = {}
        shortestPath = []
        alreadyChecked = {}
        values = {}
        for row in scope:
            for square in row:
                i, j = int(square.objectName().split('-')[1]), int(square.objectName().split('-')[2])
                values[(i, j)] = math.inf
                alreadyChecked[(i, j)] = False
        values[(int(start[0]), int(start[1]))] = 0
        alreadyChecked[(int(start[0]), int(start[1]))] = True
        recentlyChecked = [(int(start[0]), int(start[1]))]
        scope[int(start[0])][int(start[1])].setStyleSheet(self.checkedStr)
        time.sleep(0.01)
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
                            scope[square[0]][square[1]].setStyleSheet(self.beforeCheckStr)
                            time.sleep(0.01)
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
                        scope[square[0]][square[1]].setStyleSheet(self.pathStr)
                        time.sleep(0.01)
                    return

            recentlyChecked = []
            for square in toBeChecked:
                recentlyChecked.append(square)
                scope[square[0]][square[1]].setStyleSheet(self.checkedStr)
                time.sleep(0.01)
