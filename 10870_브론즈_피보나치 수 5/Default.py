num = int(input())
f1, f2, f3= 0, 1, 1
if num == 0:
  print(f1)
elif num == 1:
  print(f2)
else:
  for _ in range(0,num-1):
    f3 = f1 + f2
    f1 = f2
    f2 = f3
  print(f3)
