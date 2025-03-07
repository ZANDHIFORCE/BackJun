#dp[i] = min(dp[i-1]+1,dp[i/2)+1,dp[i/3]+1)

N = int(input())
dp = [0,0,1,1]

for i in range(4,N+1):
    m1 = dp[i-1] + 1
    m2 = N+1 if i%2!=0  else dp[i//2] + 1
    m3 = N+1 if i%3!=0  else dp[i//3] + 1
    dp.append(min(m1,m2,m3)) 
    
print(dp[N])