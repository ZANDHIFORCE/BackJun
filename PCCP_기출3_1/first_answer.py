from collections import Counter

def solution(points, routes):
    for i in range(len(points)):
        for j in range(2):
            points[i][j] = points[i][j] - 1
    for i in range(len(routes)):
        for j in range(len(routes[0])):
            routes[i][j] = routes[i][j] - 1
            
    locate_list = []
    for route in routes:
        locate_list.append(points[route[0]][:])
        
    robot_in = [True for i in range(len(routes))]
    counter = check_danger(locate_list, robot_in)
    n_list = [1 for i in range(len(routes))]
    while sum(robot_in):
        for i in range(len(locate_list)):
            next_goal = points[routes[i][n_list[i]]]
            if  n_list[i] == len(routes[i]) - 1 and locate_list[i] == points[routes[i][-1]]:
                robot_in[i] = False
            if robot_in[i]:
                if locate_list[i][0] > next_goal[0]:
                    locate_list[i][0] -=1
                elif locate_list[i][0] < next_goal[0]:
                    locate_list[i][0] +=1
                elif locate_list[i][1] > next_goal[1]:
                    locate_list[i][1] -=1
                elif locate_list[i][1] < next_goal[1]:
                    locate_list[i][1] +=1
                if locate_list[i] == next_goal and n_list[i]<len(routes[i])-1:
                    n_list[i] += 1
        counter += check_danger(locate_list, robot_in)
    answer = counter
    return answer

def check_danger(locate_list, robot_in):
    locate_counter = Counter(tuple(l) for l, r in zip(locate_list, robot_in) if r)
    # print(locate_counter)
    counter = 0
    for x in locate_counter.values():
        if x >=2:
            counter += 1
    return counter

