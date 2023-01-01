import sys

class Vertex:
    def __init__(self, value):
        self.value = value
        self.list = []
        self.visit = False
    def __str__(self):
        return self.value
    def ShowList(self):
        print(self.list)
    def Visit(self):
        self.visit =True

class App:
    def __init__(self):
        self.numberOfVertex = 0
        self.numberOfEdge = 0

        self.vertexList = []
        
        self.numberOfInfaction = 0
    
    def Run(self):
        self.InputData()
        # self.ShowMap()
        self.DFS(1)
        print(self.numberOfInfaction-1)

    def InputData(self):
        self.numberOfVertex = int(input())
        for x in range(1,self.numberOfVertex+1):
            self.vertexList.append(Vertex(x))

        self.numberOfEdge = int(input())
        for x in range(self.numberOfEdge):
            value1, value2 = map(int, sys.stdin.readline().strip().split(' '))
            index1 = self.FindIndex(value1)
            index2 = self.FindIndex(value2)
            self.vertexList[index1].list.append(value2)
            self.vertexList[index2].list.append(value1)

    def FindIndex(self, value):
        for x in range(self.numberOfVertex):
            if self.vertexList[x].value == value:
                return x
        return -1

    def ShowMap(self):
        for x in range(len(self.vertexList)):
            print(self.vertexList[x].value,": ",end='') 
            self.vertexList[x].ShowList()
    
    def DFS(self,value):
        index = self.FindIndex(value)
        self.vertexList[index].Visit()
        self.numberOfInfaction += 1
        for x in self.vertexList[index].list:
            if self.vertexList[self.FindIndex(x)].visit == False:
                self.DFS(x)


        


"""
7
6
1 2
2 3
1 5
5 2
5 6
4 7
"""

app = App()
app.Run()