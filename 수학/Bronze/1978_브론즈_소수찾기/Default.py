#file = open("test.txt","r")

input_str = input() #file.readline()
input_str = input() #file.readline()
num_list = list(map(int, input_str.split(" ")))
count = 0
for x in num_list:
  if x == 1:
    count-=1
  elif x == 2:
    pass
  else:
    for i in range(2,x):
      if x % i == 0:
        #print(x,"%",i)
        count -=1
        break;
  count+=1
print(count)
