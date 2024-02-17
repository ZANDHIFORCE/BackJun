#file = open('test.txt','r')
input_str = input()#file.readline()

for _ in range(int(input_str)):
  num_list = list(map(int, input().split(" ")))
  for _ in range(3):
    max = num_list[0]
    for x in num_list:
      if max < x:
        max = x
    num_list.remove(max)
  print(max)

