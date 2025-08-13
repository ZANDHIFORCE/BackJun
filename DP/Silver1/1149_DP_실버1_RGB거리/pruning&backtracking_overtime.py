N  = int(input())

RGB_list = [[0,0,0]]

for i in range(N):
    a, b, c = map(int, input().split())
    RGB_list.append([a,b,c])

min_value = float('inf')

def getSum(level, RGB, sum, RGB_list):
    global min_value
    if level <= N:
        sum += RGB_list[level][RGB]
        if min_value < sum:
            return
        for i in range(3):
            if RGB != i:
                getSum(level+1,i,sum,RGB_list)
    elif level == N+1:
        min_value = min(min_value, sum)

for i in range(3):
    getSum(1,i,0,RGB_list)

print(min_value)
