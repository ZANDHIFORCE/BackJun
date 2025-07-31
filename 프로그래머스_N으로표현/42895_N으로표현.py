"""
프로그래머스 - N으로 표현
동적계획법(Dynamic Programming)

문제: 숫자 N과 사칙연산만을 사용해서 number를 표현할 때, N 사용횟수의 최솟값을 구하기
제한: N은 1~9, number는 1~32000, 최솟값이 8보다 크면 -1 반환

해법: DP를 이용하여 N을 i번 사용해서 만들 수 있는 모든 수를 저장
- dp[i]: N을 i번 사용해서 만들 수 있는 모든 수들의 집합
- 각 단계에서 dp[j]와 dp[i-j]의 조합으로 새로운 수 생성

시간복잡도: O(8^3) - 최대 8단계까지만 계산
공간복잡도: O(S) - S는 생성되는 모든 수의 개수
"""

def solution(N, number):
    # 예외 처리: N 한 번으로 만들 수 있는 경우
    if number == N:
        return 1
    
    # dp 초기화
    dp = []
    dp.append([0])  # dp[0] - 사용하지 않음
    dp.append([N])  # dp[1] - N을 1번 사용
    
    # dp[2]부터 dp[8]까지 계산
    for idx in range(2, 9):
        temp_list = set()
        
        # N을 idx번 연속으로 붙인 수 (NN, NNN, NNNN, ...)
        v0 = get_consecutive_n(idx, N)
        if v0 == number:
            return idx
        temp_list.add(v0)
        
        # dp[x]와 dp[y]의 조합으로 새로운 수 생성 (x + y = idx)
        for x in range(1, idx):
            y = idx - x
            for i in range(len(dp[x])):
                for j in range(len(dp[y])):
                    # 사칙연산 수행
                    v1 = dp[x][i] + dp[y][j]  # 덧셈
                    v2 = dp[x][i] - dp[y][j]  # 뺄셈
                    v3 = dp[x][i] * dp[y][j]  # 곱셈
                    v4 = -1 if dp[y][j] == 0 else dp[x][i] // dp[y][j]  # 나눗셈
                    
                    # 목표 수를 찾았으면 즉시 반환
                    if number in [v1, v2, v3, v4]:
                        return idx
                    
                    # 결과를 temp_list에 추가
                    temp_list.add(v1)
                    temp_list.add(v2)
                    temp_list.add(v3)
                    if v4 != -1:
                        temp_list.add(v4)
        
        dp.append(list(temp_list))
    
    return -1

def get_consecutive_n(num, N):
    """N을 num번 연속으로 붙인 수를 반환 (예: N=5, num=3 -> 555)"""
    base = ''
    for _ in range(num):
        base += str(N)
    return int(base)

# 테스트 케이스
if __name__ == "__main__":
    # 예제 1: N=5, number=12, 예상결과=4
    print(solution(5, 12))  # 4
    
    # 예제 2: N=2, number=11, 예상결과=3  
    print(solution(2, 11))  # 3