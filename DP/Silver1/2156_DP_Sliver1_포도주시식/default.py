import sys
N = int(sys.stdin.readline().strip())

wine_list = [0] * (N + 1)
for i in range(1, N + 1):
    wine_list[i] = int(sys.stdin.readline().strip())

dp = [[0 for j in range(2)] for i in range(N)]

if N==1:
    print(wine_list[0])
    sys.exit()
elif N==2:
    print(wine_list[0] + wine_list[1])
    sys.exit()

dp[0][0] = wine_list[0]
dp[0][1] = 0
dp[1][0] = wine_list[1]
dp[1][1] = wine_list[1]+dp[0][0]

answer = 0
for i in range(2,N):
    dp[i][0] = wine_list[i] + max(dp[i-2][0], dp[i-2][1])
    dp[i][1] = wine_list[i] + dp[i-1][0]
    answer = max(dp[i][0], dp[i][1], answer)

print(answer)

        
