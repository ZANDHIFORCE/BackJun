class Vertex:
    def __init__(self):
        self.connect = []
        self.visit = False

class App:
    def __init__(self,f):
        self.vertexList = []
        self.vertexNum = 0
        self.edgeNum = 0
        self.count = -1
        self.f = f

    def InputData(self):
        self.vertexNum, self.edgeNum = map(int, self.f.readline().strip().split())
        for i in range(self.vertexNum):
            self.vertexList.append(Vertex())
        
        for i in range(self.edgeNum):
            index1, index2 = map(int,self.f.readline().strip().split())
            index1, index2 = index1-1, index2-1
            self.Connect(index1,index2)

    def Connect(self,index1,index2):
        self.vertexList[index1].connect.append(index2)
        self.vertexList[index2].connect.append(index1)

    def DFS(self,index):
        self.vertexList[index].visit = True
        self.count+=1

        for x in self.vertexList[index].connect:
            if not self.vertexList[x].visit:
                self.DFS(x)

    def PrintCount(self):
        print(self.count)
            

        



        
f = open("test.txt",'r')
number = int(f.readline().strip())
for i in range(number):
    app = App(f)
    app.InputData()
    app.DFS(0)
    app.PrintCount()


class Vertex:
    def __init__(self):
        self.connect = []
        self.visit = False

class App:
    def __init__(self,f):
        self.vertexList = []
        self.vertexNum = 0
        self.edgeNum = 0
        self.count = -1
        self.f = f

    def InputData(self):
        self.vertexNum, self.edgeNum = map(int, self.f.readline().strip().split())
        for i in range(self.vertexNum):
            self.vertexList.append(Vertex())
        
        for i in range(self.edgeNum):
            index1, index2 = map(int,self.f.readline().strip().split())
            index1, index2 = index1-1, index2-1
            self.Connect(index1,index2)

    def Connect(self,index1,index2):
        self.vertexList[index1].connect.append(index2)
        self.vertexList[index2].connect.append(index1)

    def DFS(self,index):
        self.vertexList[index].visit = True
        self.count+=1

        for x in self.vertexList[index].connect:
            if not self.vertexList[x].visit:
                self.DFS(x)

    def PrintCount(self):
        print(self.count)
            

        



        
f = open("test.txt",'r')
number = int(f.readline().strip())
for i in range(number):
    app = App(f)
    app.InputData()
    app.DFS(0)
    app.PrintCount()


