class App:
    def __init__(self):
        self.size = 0
        self.weight = 0
        self.item = []

    def InputData(self):
        f = open("test.txt",'r')
        self.size, self.weight = map(int,f.readline().strip().split())
        for i in range(self.size):
            size , value = map(int,f.readline().strip().split())
            self.item.append((size,value))
        
    def Sort(self):
        value = 0
        for i in range(self.size-1,0,-1):
            for j in range(0,i,+1):
                if self.GetValue(self.item[j]) < self.GetValue(self.item[j+1]):
                    self.item[j] , self.item[j+1] = self.item[j+1] , self.item[j]
        print(self.item)

    def GetValue(self, item):
        return item[1]/item[0]
            

app =App()
app.InputData()
app.Sort()