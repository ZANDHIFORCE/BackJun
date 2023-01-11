import sys
class Vertex:
    def __init__(self):
        self.value = 0
        self.visit = False
        self.connect = []

class App:
    def __init__(self,f):
        self.vNum = 0
        self.eNum = 0
        self.vList = []

        self.start = 0
        self.end = 0

        self.f = f
    
    def InputData(self):
        self.vNum = int(self.f.readline().strip())
        self.eNum = int(self.f.readline().strip())
        
        for i in range(self.vNum):
            self.vList.append(Vertex())

        for i in range(self.eNum):
            index1, index2, value = map(int,self.f.readline().strip().split())
            index1, index2 = index1-1, index2-1
            self.Connect(index1, index2, value)

        self.start , self.end = map(int,self.f.readline().strip().split())
        self.start , self.end = self.start-1, self.end-1

    def Connect(self, index1, index2, value):
        self.vList[index1].connect.append([index2,value])

    def BFS(self):
        queue = []
        queue.append(self.start)
        self.vList[self.start].visit=True

        while queue:
            print(queue)
            index = queue.pop(0)

            for x in self.vList[index].connect:
                if not self.vList[x[0]].visit or self.vList[x[0]].value > self.vList[index].value+x[1]:
                    if x[0] not in queue:
                        queue.append(x[0])
                    self.vList[x[0]].visit = True
                    self.vList[x[0]].value = self.vList[index].value+x[1]

        print(self.vList[self.end].value)

    def PrintValue(self):
        for x in self.vList:
            print(x.value,'',end='')
        print()



f = open("test.txt",'r')
app = App(f)
app.InputData()
app.BFS()