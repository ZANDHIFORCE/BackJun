class Vertex:
    def __init__(self,i,j):
        self.i = i
        self.j = j


class Map:
    def __init__(self,row,col):
        self.row = row
        self.col = col
        self.data = []
        self.virusqueue = []
    
    def SetVirus(self):
        for i in range(self.row):
            for j in range(self.col):
                if self.data[i][j]=='2':
                    self.virusqueue.append(Vertex(i,j))
                    print(i,j)


    def Printdata(self):
        for row in self.data:
            print(row)
        


class App:
    
    def __init__(self):
        self.mapList=[]

    def Inputdata(self):
        f = open("test.txt" ,"r")
        row, col = map(int,f.readline().strip().split())

        tempMap = Map(row,col)
        for i in range(col):
            tempLine = f.readline().strip()
            tempMap.data.append(tempLine)
            
        tempMap.SetVirus()
        self.mapList.append(tempMap)

    def Run(self):
        self.Inputdata()


app = App()

app.Run()