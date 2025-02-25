def w(a, b, c):
    print("w","(",a, b, c,")")
    if a<=0 or b<= 0 or c<= 0:
        return 1
    if a>20 or b>20 or c>20:
        return w(20,20,20)
    if a<b and b<c:
        return w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    
    return w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)

def normalize_abc(coor):
    if coor['a'] <= 0 or coor['b'] <= 0 or coor['c'] <= 0:
        coor['a'] = coor['b'] = coor['c'] = 0
    elif coor['a'] > 0 or coor['b'] > 20 or coor['c'] > 20:
        coor['a'] = coor['b'] = coor['c'] = 20

n = 5

w_list = [[[0 for k in range(n+1)] for j in range(n+1)] for i in range(n+1)]

for i in range(n+1):
    for j in range(n+1):
        for k in range(n+1):
            if i == 0 or j == 0 or k ==0:
                w_list[i][j][k] = 1



