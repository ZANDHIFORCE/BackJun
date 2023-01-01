import sys

class Vertex:
    def __init__(self,value):
        self.value = value
        self.count = 0
        self.visited = False

class App:
    def __init__(self):
        self.raw = 0
        self.col = 0
        self.map = []
    
    def InputData(self):
        f = open("test.txt", 'r')
        self.raw, self.col = map(int, f.readline().strip().split())
        tempRaw = []
        for i in range(self.raw):
            tempStr = f.readline().strip()
            for x in tempStr:
                tempRaw.append(Vertex(int(x)))
            self.map.append(tempRaw)
            tempRaw = tempRaw[:]
            tempRaw.clear()

    def CheckIndex(self,index):
        self.map[index[0]][index[1]].visited = True

    def IsChecked(self, index):
        return self.map[index[0]][index[1]].visited

    def PrintfValue(self):
        for raw in self.map:
            for x in raw:
                print(x.value, end="")
            print()

    def PrintfCount(self):
            for raw in self.map:
                for x in raw:
                    print(x.count, end="")
                print()
        


    def BFS(self):

        queue = []
        queue.append([0,0])
        self.CheckIndex([0,0])
        self.map[0][0].count+=1

        finalIndex = [self.raw-1, self.col-1]
        find = False

        dx = [1,-1,0,0]
        dy = [0,0,1,-1]

        while find == False:
            tempIndex = queue.pop(0)
            tempCount = self.map[tempIndex[0]][tempIndex[1]].count
            
            if finalIndex == tempIndex:
                find = True

            for i in range(4):
                tempx = tempIndex[0] + dx[i]
                tempy = tempIndex[1] + dy[i]
                if tempx>=0 and tempy>=0 and tempx<self.raw and tempy<self.col:
                    if self.map[tempx][tempy].value == 1 and self.IsChecked([tempx,tempy])==False:
                        queue.append([tempx,tempy])
                        self.CheckIndex([tempx,tempy])
                        self.map[tempx][tempy].count = tempCount+1

        return self.map[finalIndex[0]][finalIndex[1]].count
                
                    

        
            
        



    def Run(self):
        self.InputData()
        print(self.BFS())


app = App()

app.Run()