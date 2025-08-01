from collections import Counter

counter = Counter(map(int, input().split()))

log_list = []
for key, value in counter.items():
    log_list.append((key,value))

sorted_log_list = sorted(log_list, key = lambda x: x[1], reverse = True)
nuun, count = sorted_log_list[0]

if count==3:
    print(10000+nuun*1000)
elif count==2:
    print(1000+nuun*100)
else:
    print(max(counter.keys())*100)

