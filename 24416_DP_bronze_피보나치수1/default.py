# count1=0
# count2=0

# def fib(n):
#     global count1
#     if n==1 or n==2:
#         count1+=1
#         return n
#     else:
#         return fib(n-1)*fib(n-2)
    
# def fibonacci(n):
#     global count2
#     f = [1,1,2]
#     for x in range(2,n):
#         count2+=1
#         f.append(f[x] + f[x-1])
#     return f[n]

def count_fib(n):
    f = [1,1,2]
    for x in range(2,n):
        f.append(f[x]+f[x-1])
    return f[n-1]

def count_fibonacci(n):
    return n-2 if n-2>=0 else 0

number = int(input())

print(count_fib(number), count_fibonacci(number))