#file = open('test.txt', 'r')
input_str = input() #file.readline()

num1, num2 = map(int, input_str.split(' '))

if num1>num2:
  _ = num1
  num1 = num2
  num2 = _

result1 = 1
for x in range(num1, 1, -1):
  if num1%x==0 and num2%x==0:
    result1 = x
    num1, num2 = int(num1/x), int(num2/x)
    break

result2 = result1*num1*num2

print(result1)
print(result2)
