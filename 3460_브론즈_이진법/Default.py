#file = open('test.txt','r')

input_str = input()  #file.readline()

result = []

for _ in range(int(input_str)):
  num = int(input())  #int(file.readline())
  while num != 0:
    result.append(num % 2)
    num = int(num / 2)

  for i in range(len(result)):
    if result[i] == 1:
      print(i, end=" ")
  print('\b')
  result.clear()
