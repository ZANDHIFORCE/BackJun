import sys

class Vertex:
    def __init__(self,  value):
        self.value = value
        self.visited = False

class Map:
    def __init__(self):
        self.row = 0
        self.col = 0
        self.map  = []
        self.num = 0

    def InputData(self):
        self.row, self.col, self.num = map(int,sys.stdin.readline().strip().split())

        vertexList = []
        for i in range(self.row):
            for j in range(self.col):
                vertexList.append(Vertex(0))
            self.map.append(vertexList)
            vertexList = vertexList[:]
            vertexList.clear()

        for i in range(self.num):
            x, y = map(int, sys.stdin.readline().strip().split())
            self.SetOne(x,y)

    def SetOne(self,i,j):
        self.map[i][j].value = 1

    def BFS(self, x, y, value):
        queue = []
        queue.append([x,y])
        self.map[x][y].visited = True
        self.map[x][y].value = value

        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        while queue:
            temp = queue.pop(0)
            originX, originY = temp[0], temp[1]
            for i in range(4):
                nextX = originX +dx[i]
                nextY = originY +dy[i]
                if nextX>=0 and nextY>=0 and nextX<self.row and nextY<self.col:
                    if self.map[nextX][nextY].visited == False and self.map[nextX][nextY].value==1:
                        queue.append([nextX,nextY])
                        self.map[nextX][nextY].visited = True
                        self.map[nextX][nextY].value = value

    def GetMax(self):
        Max = 0
        for row in self.map:
            for x in row:
                if x.value > Max:
                    Max = x.value
        return Max

    def FindOne(self):
        for i in range(self.row):
            for j in range(self.col):
                if self.map[i][j].value == 1 and self.map[i][j].visited == False:
                    return i,j
        return -1,-1

    def Infest(self):
        value = 1
        while self.FindOne() != (-1,-1):
            tempx , tempy = self.FindOne()
            self.BFS(tempx,tempy,value)
            value+=1

    def PrintMapValue(self):
        for row in self.map:
            for x in row:
                print(x.value,end="")
            print()


class App:
    def __init__(self):
        self.mapList  = []

    def InputData(self):
        num = int(input())
        for i in range(num):
            tempMap = Map()
            tempMap.InputData()
            self.mapList.append(tempMap)

    def PrintResult(self):
        for map in self.mapList:
            map.Infest()
            print(map.GetMax())

    def Run(self):
        self.InputData()
        self.PrintResult()


app =App()
app.Run()