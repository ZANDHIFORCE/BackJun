class App:
    def __init__(self):
        self.list = []
        self.size = 0
        self.value = 0

    def InputData(self):
        f = open("test.txt", 'r')
        self.size = int(f.readline().strip())
        self.list = list(map(int,f.readline().strip().split()))

    def Delete(self):
        for i in range(self.size):
            if self.list[i]:
                while self.Delete3(i):
                    pass
                while self.Delete2(i):
                    pass
                while self.Delete1(i):
                    pass
    
    def PrintValue(self):
        print(self.list)
        print(self.value)

    def Delete1(self,i):
        if self.list[i]:
            self.value+=3
            self.list[i]-=1
            return True
        return False
    
    def Delete2(self,i):
        if i<self.size-1 and self.list[i] and self.list[i+1]:
            self.value+=5
            self.list[i]-=1
            self.list[i+1]-=1
            return True
        return False

    def Delete3(self,i):
        if i<self.size-2 and self.list[i] and self.list[i+1] and self.list[i+2]:
            self.value+=7
            self.list[i]-=1
            self.list[i+1]-=1
            self.list[i+2]-=1
            return True
        return False
    
                        


app = App()
app.InputData()
app.Delete()
app.PrintValue()
    