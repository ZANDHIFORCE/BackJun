N = int(input())

wine_list = []
for i in range(N):
    wine_list.append(int(input()))

dp = [[0 for j in range(2)] for i in range(N)]

if N == 1:
    print(wine_list[0])
    quit()
elif N == 2:
    print(sum(wine_list))
    quit()

dp[0][0] = wine_list[0]  # i=0, [0][0] = 100
dp[0][1] = 0
dp[1][0] = wine_list[1]  # i=1, [1][0] = 1
dp[1][1] = wine_list[1] + dp[0][0]  # i=1, [1][1] = 1 + 100 = 101

answer = 0
print(f"i=-1 => answer={answer}")

for i in range(2, N):
    dp[i][0] = wine_list[i] + max(dp[i-2])       # 현재 잔만 마시고, i-2 중 max인 것과 더함
    dp[i][1] = wine_list[i] + dp[i-1][0]         # 이전 잔도 마셨기 때문에 i-1은 [0]상태여야 함
    answer = max(dp[i][0], dp[i][1], answer)

    print(f"i={i} => dp[i][0]={dp[i][0]}, dp[i][1]={dp[i][1]}, answer={answer}")

print("final answer =", answer)
