def w(a, b, c):
    print("w","(",a, b, c,")")
    if a<=0 or b<= 0 or c<= 0:
        return 1
    if a>20 or b>20 or c>20:
        return w(20,20,20)
    if a<b and b<c:
        return w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    
    return w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    

w_list = [[[-1 for k in range(3)] for j in range(3)] for i in range(3)]

print(w_list)

    

