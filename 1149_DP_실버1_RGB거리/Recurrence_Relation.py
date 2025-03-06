N  = int(input())

RGB_list = []

for i in range(N):
    RGB_list.append(list(map(int, input().split())))
    
dp = [[RGB_list[0][i] for i in range(3)]]


for i in range(1,N):
    temp_list = []
    for j in range(3):
        temp_list.append(min(dp[i-1][k] for k in range(3) if k != j) + RGB_list[i][j])
    dp.append(temp_list)
    
print(min(dp[N-1]))