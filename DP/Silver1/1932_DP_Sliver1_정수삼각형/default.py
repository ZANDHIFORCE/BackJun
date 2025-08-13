N = int(input())

triangle = []

for i in range(N):
    triangle.append(list(map(int,input().split())))

dp = []

dp.append(triangle[0])
for i in range(1,N):
    temp_list = []
    for j in range(len(triangle[i])):
        mother_node = 0 if j-1<0 else dp[i-1][j-1]
        father_node = 0 if j>=len(triangle[i-1]) else dp[i-1][j]
        temp_list.append(max(mother_node, father_node) + triangle[i][j])
    dp.append(temp_list)
    
print(max(dp[N-1]))