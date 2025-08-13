# 0	빈칸
# 1	빨간 수레의 시작 칸
# 2	파란 수레의 시작 칸
# 3	빨간 수레의 도착 칸
# 4	파란 수레의 도착 칸
# 5	벽
# 6 파란 수레 빨간 수레의 중복 지나온 칸
# 7 빨간 수레가 지나온 곳
# 8 파란 수레가 지나온 곳

def solution(maze):
    answer = 0
    #위치 찾기
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            #빨간수레 시작위치
            if maze[i][j] == 1:
                red_c = (i,j)
                maze[i][j] = 0
            #파란수레 시작위치
            if maze[i][j] == 2:
                blue_c = (i,j)
                maze[i][j] = 0
            #빨간수레 도착지점
            if maze[i][j] == 3:
                red_goal = (i,j)
                maze[i][j] = 0
            #파란수레 도착지점
            if maze[i][j] == 4:
                blue_goal = (i,j)
                maze[i][j] = 0
    
    mildstone = [float('inf')]
    copy_maze = [x[:] for x in maze]
    DFS(red_c, blue_c, red_goal, blue_goal, 0, mildstone, copy_maze)
    if mildstone[0] == float('inf'):
        mildstone[0] = 0
    return mildstone[0]

def DFS(red_c, blue_c, red_goal, blue_goal, count, mildstone, maze):
    #print_m(maze)
    #마일드스톤 넘으면 종료
    if mildstone[0] <= count:
        return None
    #둘다 도착하면 mildstone 설정하고 종료
    if red_c == red_goal and blue_c == blue_goal:
        mildstone[0] = min(count ,mildstone[0])
        return None
    
    #좌표안에 있는건지 검사
    if is_in(red_c, maze) and is_in(blue_c, maze):
        ri, rj = red_c
        bi, bj = blue_c
        red_validate = [0, 3, 8]
        blue_validate = [0, 4, 7]
        #유효성 검사
        if (maze[ri][rj] in red_validate) and (maze[bi][bj] in blue_validate) and red_c!=blue_c:
            past_red_block = maze[ri][rj]
            past_blue_block = maze[bi][bj]
            # maze[ri][rj] = 1
            # maze[bi][bj] = 2
            # print(f"시간: {count}")
            # print_m(red_c,blue_c,red_goal,blue_goal,maze)
            #모든 경우의 수 좌표 이동
            move_list = [(0,-1), (0,1), (-1,0), (1,0)]
            for move in move_list:
                if red_c != red_goal:
                    dri = ri + move[0]
                    drj = rj + move[1]
                else:
                    dri = ri
                    drj = rj
                dr_coor = (dri, drj)
                for move in move_list:
                    if blue_c != blue_goal:
                        dbi = bi + move[0]
                        dbj = bj + move[1]
                    else:
                        dbi = bi
                        dbj = bj
                    db_coor = (dbi, dbj)
                    #지나온 곳 후처리
                    if red_c == red_goal:
                         maze[ri][rj] = 3
                    else:
                        maze[ri][rj] = 6 if past_red_block == 8 else 7
                    if blue_c == blue_goal:
                        maze[ri][rj] = 4
                    else:
                        maze[bi][bj] = 6 if past_blue_block == 7 else 8
                    #재귀
                    copy_maze = [x[:] for x in maze]
                    #충돌방지
                    #if dr_coor != blue_c or db_coor != red_c:
                    if dr_coor != blue_c or db_coor != red_c:
                        DFS(dr_coor, db_coor, red_goal, blue_goal, count+1, mildstone, copy_maze)
def print_m(red_c,blue_c,red_goal,blue_goal,maze):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if (i,j) == red_c:
                print(1 ,end=" ")
            elif (i,j) == blue_c:
                print(2 ,end=" ")
            elif (i,j) == red_goal:
                print(3, end=" ")
            elif (i,j) == blue_goal:
                print(4, end=" ")
            else:
                print(maze[i][j] ,end=" ")
        print()
    print()
                    
def is_in(coor, maze):
    i ,j = coor
    return 0<= i < len(maze) and 0<= j < len(maze[0])