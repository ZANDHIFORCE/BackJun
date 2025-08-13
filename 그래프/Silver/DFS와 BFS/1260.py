import sys

class Vertex:
    def __init__(self, value):
        self.value = value
        self.connectList = []
        self.visited = False


class APP:

    def __init__(self):
        self.vertexList = []
        self.vertexNum = -1
        self.edgeNum = -1
        self.startPoint = -1
    
    def Run(self):
        self.InputData()
        # self.PrintVertex()
        self.DFS(self.startPoint)
        print()

        self.ClearVisited()

        self.BFS(self.startPoint)
        print()


    def InputData(self):
        # f = open("test.txt","r")

        self.vertexNum, self.edgeNum, self.startPoint= map(int, sys.stdin.readline().strip().split())
        for x in range(1, self.vertexNum+1):
            self.vertexList.append(Vertex(x))

        for x in range(self.edgeNum):
            num1, num2 = map(int, sys.stdin.readline().strip().split())
            self.Edging(num1, num2)

        for vertex in self.vertexList:
            vertex.connectList.sort()

    def Edging(self, value1, value2):
        index1 = self.FindIndex(value1)
        index2 = self.FindIndex(value2)
        self.vertexList[index1].connectList.append(value2)
        self.vertexList[index2].connectList.append(value1)
        
    def FindIndex(self, value):
        count = 0
        for x in self.vertexList:
            if x.value == value:
                return count
            count += 1
        return -1
            
    def PrintVertex(self):
        for vertex in self.vertexList:
            print(vertex.value,": ",vertex.connectList)

    def ClearVisited(self):
        for vertex in self.vertexList:
            vertex.visited = False

    def DFS(self, startPoint):
        print(startPoint,'', end='')
        startIndex = self.FindIndex(startPoint)
        self.vertexList[startIndex].visited = True
        
        for value in self.vertexList[startIndex].connectList:
            index = self.FindIndex(value)
            if self.vertexList[index].visited == False:
                self.DFS(value)

    def BFS(self, startPoint):
        queue = []
        queue.append(startPoint)
        self.vertexList[self.FindIndex(startPoint)].visited=True

        while queue:
            value = queue.pop(0)
            popIndex = self.FindIndex(value)
            print(value,'',end='')
            for value in self.vertexList[popIndex].connectList:
                conectedIndex = self.FindIndex(value)
                if self.vertexList[conectedIndex].visited==False:
                    self.vertexList[self.FindIndex(value)].visited=True
                    queue.append(value)
            


        


        
        


app = APP()

app.Run()

