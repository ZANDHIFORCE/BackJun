import sys

def w(a, b, c):
    if a<=0 or b<= 0 or c<= 0:
        return 1
    if a>20 or b>20 or c>20:
        return w(20,20,20)
    if a<b and b<c:
        if w_list[a][b][c] == 0:
            w_list[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return w_list[a][b][c]
    
    if w_list[a][b][c] == 0:
        w_list[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    return  w_list[a][b][c]

def normalize_abc(coor):
    if coor['a'] <= 0 or coor['b'] <= 0 or coor['c'] <= 0:
        coor['a'] = coor['b'] = coor['c'] = 0
    elif coor['a'] > n or coor['b'] > n or coor['c'] > n:
        coor['a'] = coor['b'] = coor['c'] = n

n =20
w_list = [[[0 for i in range(n+1)] for j in range(n+1)] for k in range(n+1)]
input_data = []
output_data = []

for line in sys.stdin:
    a, b, c = map(int, line.strip().split())
    if a == b == c == -1:
        break
    input_data.append((a,b,c))

for data in input_data:
    a, b, c = data[0], data[1], data[2]
    result = w(a,b,c)
    output_data.append(f"w({a}, {b}, {c}) = {result}")

for line in output_data:
    print(line)

