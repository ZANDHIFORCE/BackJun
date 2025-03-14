N = int(input())

wine = []

for i in range(N):
    wine.append(int(input()))

if N ==1:
    print(wine[0])
elif N ==2:
    print(wine[0]+wine[1])
else:
    dp = [[0,0] for i in range(N)]
    dp[0][0], dp[0][1] = wine[0], wine[0]
    dp[1][0], dp[1][1] = wine[1], wine[0] + wine[1]

    #there are two state
    #1. -> OXO first sip dp[i][0] = wine[i] + max(dp[i-2][0],dp[i-2][1])
    #2. -> XOO second sip dp[i][1] = wine[i] + dpo[i-1][0]

    for i in range(3,N):
        dp[i][0] = wine[i] + max(dp[i-2][0],dp[i-2][1])
        dp[i][1] = wine[i] + dp[i-1][0]

    #Last sip end 
    #OXO XOO
    #second to last sip end
    #XOX OOX

    print(max(dp[N-1][0],dp[N-1][1],dp[N-2][0],dp[N-2][1]))
