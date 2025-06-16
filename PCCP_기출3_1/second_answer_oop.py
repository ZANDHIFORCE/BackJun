from collections import Counter

def solution(points, routes):
    #정규화
    normalization(points)
    normalization(routes)
    #로봇 리스트에 추가
    robots = []
    for route in routes:
        paths = []
        for p in route:
            paths.append(points[p])
        robots.append(Robot(paths))
    #로봇 이동
    while sum(robot.get_activate() for robot in robots):
        for robot in robots:
            robot.move()
    #로봇 히스토리 추출
    historys = []
    for robot in robots:
        historys.append(robot.get_history())
    #로봇 충돌 카운트
    count = 0
    for time in range(len(historys[0])):
        danger_counter = Counter()
        for history in historys:
            danger_counter.update([tuple(history[time][0:2])] if history[time][2] else ())
        count += sum(1 for v in danger_counter.values() if v>1)
    return count

def normalization(list1):
    for i in range(len(list1)):
        for j in range(len(list1[0])):
            list1[i][j] -= 1

class Robot:
    def __init__(self, paths):
        self.paths = paths
        self.r = paths[0][0]
        self.c = paths[0][1]
        self.target = 1
        self.goal_target = len(paths)-1
        self.activate = True
        self.history = [[self.r, self.c, True]]
    
    def move(self):
        if self.activate:
            
            if [self.r,self.c] == self.paths[self.target]:
                if self.target < self.goal_target:
                    self.target += 1
                else:
                    self.activate = False
                    
            target_r = self.paths[self.target][0]
            target_c = self.paths[self.target][1]  
            if self.r < target_r:
                self.r += 1
            elif self.r > target_r:
                self.r -= 1
            elif self.c < target_c:
                self.c += 1
            elif self.c > target_c:
                self.c -= 1
            else:
                pass
        self.history.append([self.r, self.c, self.activate])

    def get_history(self):
        return self.history
    
    def get_activate(self):
        return self.activate
        