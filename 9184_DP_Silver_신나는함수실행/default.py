# def w(a, b, c):
#     print("w","(",a, b, c,")")
#     if a<=0 or b<= 0 or c<= 0:
#         return 1
#     if a>20 or b>20 or c>20:
#         return w(20,20,20)
#     if a<b and b<c:
#         return w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    
#     return w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)

import sys

def normalize_abc(coor):
    if coor['a'] <= 0 or coor['b'] <= 0 or coor['c'] <= 0:
        coor['a'] = coor['b'] = coor['c'] = 0
    elif coor['a'] > n or coor['b'] > n or coor['c'] > n:
        coor['a'] = coor['b'] = coor['c'] = n

n = 20

w_list = [[[0 for k in range(n+1)] for j in range(n+1)] for i in range(n+1)]

w_list[0][0][0] = 1

for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
            coor_origin = dict(a=i,b=j,c=k)
            if coor_origin['a'] < coor_origin['b'] < coor_origin['c']:
                coor1, coor2, coor3 = dict(a=i,b=j,c=k-1), dict(a=i,b=j-1,c=k-1), dict(a=i,b=j-1,c=k)
                normalize_abc(coor1)
                normalize_abc(coor2)
                normalize_abc(coor3)
                
                if w_list[coor1['a']][coor1['b']][coor1['c']] * w_list[coor2['a']][coor2['b']][coor2['c']] * w_list[coor3['a']][coor3['b']][coor3['c']] == 0:
                    print("[ERROR]")
                
                w1 = w_list[coor1['a']][coor1['b']][coor1['c']]
                w2 = w_list[coor2['a']][coor2['b']][coor2['c']]
                w3 = w_list[coor3['a']][coor3['b']][coor3['c']]
                w_list[i][j][k] = w1 + w2 - w3
            else:
                coor4, coor5, coor6, coor7 = dict(a=i-1,b=j,c=k),dict(a=i-1,b=j-1,c=k),dict(a=i-1,b=j,c=k-1),dict(a=i-1,b=j-1,c=k-1)
                normalize_abc(coor4)
                normalize_abc(coor5)
                normalize_abc(coor6)
                normalize_abc(coor7)
                
                if w_list[coor4['a']][coor4['b']][coor4['c']] * w_list[coor5['a']][coor5['b']][coor5['c']] * w_list[coor6['a']][coor6['b']][coor6['c']] * w_list[coor7['a']][coor7['b']][coor7['c']] == 0:
                    print("[ERROR]")
                
                w4 = w_list[coor4['a']][coor4['b']][coor4['c']]
                w5 = w_list[coor5['a']][coor5['b']][coor5['c']]
                w6 = w_list[coor6['a']][coor6['b']][coor6['c']]
                w7 = w_list[coor7['a']][coor7['b']][coor7['c']]
                w_list[i][j][k] = w4 + w5 + w6 - w7
                
output_data = []
while(1):
    input_data = sys.stdin.readline().strip()
    n1, n2, n3 = map(int, input_data.split())
    if n1 == n2 == n3 == -1:
        break
    else:
        coor = dict(a=n1, b=n2, c=n3)
        normalize_abc(coor)
        output_data.append(f"w({n1}, {n2}, {n3}) = {w_list[coor['a']][coor['b']][coor['c']]}")

for line in output_data:
    print(line)

            




