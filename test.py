import sys
import copy

sys.setrecursionlimit(1000001)

class Vertex:
    def __init__(self, color):
        self.color= color
        self.sector = 0

class App:
    def __init__(self):
        self.size = 0
        self.map_1 = []
        self.map_2 = []

    def ChangeStr(self, str1):
        tempStr = ''
        for x in str1:
            if x == 'G':
                tempStr+='R'
            else:
                tempStr+=x
        return tempStr

    def DeepCopy(self, lines):
        tempLines = copy.deepcopy(lines)
        for line in tempLines:
            for x in line:
                if x.color == 'G':
                    x.color = 'R'
        return tempLines

    def ShowMapColor(self, map):
        for line in map:
            for x in line:
                print(x.color, end='')
            print()

    def ShowMapSector(self, map):
        for line in map:
            for x in line:
                print(x.sector, end='')
            print()
    
    def InputData(self):
        self.size = int(input())
        lines = []
        line = []
        for i in range(self.size):
            tempstr = sys.stdin.readline().strip()
            for j in tempstr:
                line.append(Vertex(j))
            lines.append(line)
            line = line[0:0]
        self.map_1 = lines
        self.map_2 = self.DeepCopy(lines)

    def FindIndex(self, map):
        for i in range(self.size):
            for j in range(self.size):
                if map[i][j].sector == 0:
                    return (i,j)
        return (-1,-1)

    def Check(self, i, j, sector, map):
        map[i][j].sector = sector

        #상
        if i-1>=0 and map[i][j].color == map[i-1][j].color and map[i-1][j].sector==0:
            self.Check(i-1, j, sector, map)
        #하
        if i+1<self.size and map[i][j].color == map[i+1][j].color and map[i+1][j].sector==0:
            self.Check(i+1, j, sector, map)
        #좌
        if j-1>=0 and map[i][j].color == map[i][j-1].color and map[i][j-1].sector==0:
            self.Check(i, j-1, sector, map)
        #우
        if j+1<self.size and map[i][j].color == map[i][j+1].color and map[i][j+1].sector==0:
            self.Check(i, j+1, sector, map)

    def DFS(self, map):
        sector = 0
        while self.FindIndex(map) != (-1,-1):
            sector+=1
            i, j = self.FindIndex(map)
            self.Check(i, j, sector, map)
        return sector


    def Run(self):
        self.InputData()
        print(self.DFS(self.map_1),self.DFS(self.map_2),end='')

"""
5
RRRBB
GGBBB
BBBRR
BBRRR
RRRRR

"""

app = App()
app.Run()




