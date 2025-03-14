#OX      dp[i] = dp[i-1]
#OXO     dp[i] = wine[i] + dp[i-2]
#OXOO    dp[i] = wine[i] + wine[i-1] + dp[i-3]

N = int(input())

wine = []

for i in range(N):
    wine.append(int(input()))

dp =[0]*N
if N ==1:
    print(wine[0])
elif N==2:
    print(wine[0]+wine[1])
else:
    dp[0] = wine[0]
    dp[1] = wine[0] + wine[1]
    dp[2] = max(wine[0]+wine[1],wine[0]+wine[2],wine[1]+wine[2])
    # OOX
    # OXO
    # XOO
    for i in range(3,N):
        dp[i] = max(dp[i-1], wine[i]+dp[i-2], wine[i]+wine[i-1]+dp[i-3])
    print(dp[N-1])

