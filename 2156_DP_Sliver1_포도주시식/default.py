N = int(input())

wine_list = []
for i in range(N):
    wine_list.append(int(input()))

dp = [[0 for j in range(2)] for i in range(N)]

if N==1:
    print(wine_list[0])
    quit()
elif N==2:
    print(sum(wine_list))
    quit()

dp[0][0] = wine_list[0]
dp[0][1] = 0
dp[1][0] = wine_list[1]
dp[1][1] = wine_list[1]+dp[0][0]

max_value = dp[1][1]

for i in range(2,N):
    dp[i][0] = wine_list[i] + max(dp[i-2])
    dp[i][1] = wine_list[i] + dp[i-1][0]
    
max_value = max(dp[N-1]+dp[N-2]+ dp[N-3])

print(max_value)

        
