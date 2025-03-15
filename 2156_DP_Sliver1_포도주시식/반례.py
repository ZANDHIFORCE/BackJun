N = 10

wine = [100, 100, 1, 1, 100, 100, 1, 1, 100, 100]

#for i in range(N):
    #wine.append(int(input()))

if N ==1:
    print(wine[0])
elif N ==2:
    print(wine[0]+wine[1])
else:
    dp = [[0,0] for i in range(N)]

    #there are two state
    #1. OXO first sip dp[i][0] = wine[i] + max(dp[i-2][0],dp[i-2][1])
    #2. XOO second sip dp[i][1] = wine[i] + dpo[i-1][0]

    for i in range(3,N):
        dp[i][0] = wine[i] + max(dp[i-2][0],dp[i-2][1])
        dp[i][1] = wine[i] + dp[i-1][0]

    #Last sip end 
    #OXO XOO
    #second to last sip end
    #XOX OOX

    print(max(dp[N-1][0],dp[N-1][1],dp[N-2][0],dp[N-2][1]))


#for i in range(N):
    #wine.append(int(input()))

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

