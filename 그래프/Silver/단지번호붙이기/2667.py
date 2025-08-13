import sys
class App:
    def __init__(self):
        self.map = []
        self.row = 0

    def InputData(self):
        f = open("test.txt",'r')
        self.row = int(f.readline().strip())
        tempIntList = []
        for x in range(self.row):
            tempLine = f.readline().strip()
            for y in tempLine:
                tempIntList.append(int(y))
            self.map.append(tempIntList)
            tempIntList = tempIntList[:]
            tempIntList.clear()
        

    def BFS(self, x, y, number):
        queue = [[x,y]]
        self.map[x][y] = number

        dx = [-1,1,0,0]
        dy = [0,0,1,-1]

        while queue:
            index = queue.pop(0)
            tempIndex = [0,0]
            
            for i in range(4):
                tempIndex[0] = index[0]+dx[i]
                tempIndex[1] = index[1]+dy[i]
                if tempIndex[0]>=0 and tempIndex[1]>=0 and tempIndex[0]<self.row and tempIndex[1]<self.row:
                    if self.map[tempIndex[0]][tempIndex[1]]==1:
                        queue.append(tempIndex)
                        self.map[tempIndex[0]][tempIndex[1]] = number
                        tempIndex = tempIndex[:]

    def Infest(self):
        number = 2

        while self.FindOne() != (-1,-1):
            index = self.FindOne()
            self.BFS(index[0],index[1],number)
            number +=1

    def PrintResult(self):
        max = self.FindMax()
        print(max-1)

        numList = []

        for i in range(2,max+1):
            count = 0
            for row in self.map:
                for x in row:
                    if x==i:
                        count+=1
            numList.append(count)

        numList.sort()
        for x in numList:
            print(x)
        
        

    def PrintMap(self):
        for row in self.map:
            print(row)
        print()
                
    def Run(self):
        self.InputData()
        self.Infest()
        self.PrintResult()

    def FindOne(self):
        for i in range(self.row):
            for j in range(self.row):
                if self.map[i][j] == 1:
                    return i,j
        
        return -1,-1

    def FindMax(self):
        max = -1
        for row in self.map:
            for x in row:
                if x > max:
                    max = x
        return max


app = App()

app.Run()