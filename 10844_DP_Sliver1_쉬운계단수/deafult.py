# dp[i][j] = dp [i-1][j-1] + dp[i-1][j+1]

dp = [[0 for j in range(10)]for i in range(101)]

for j in range(10):
    dp[1][j] = 1
    
N = int(input())

for i in range(2,N+1):
    for j in range(10):
        left =  0 if j-1<0 else dp[i-1][j-1]
        right = 0 if j+1>9 else dp[i-1][j+1]
        dp[i][j] = (left + right)%1000000000
        
print(sum(dp[N][1:])%1000000000)