N = int(input())

stair_list = []
for i in range(N):
    stair_list.append(int(input()))
    
dp = [[0 for j in range(2)] for i in range(N)]

dp[0][0] = stair_list[0]

for i in range(1,N):
    dp[i][0] = stair_list[i] + max(0 if i-2 < 0 else dp[i-2][0], dp[i-2][1])
    dp[i][1] = stair_list[i] + dp[i-1][0]

print(max(dp[N-1]))