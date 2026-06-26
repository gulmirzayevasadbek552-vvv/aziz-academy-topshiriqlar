n = int(input())
a = list(map(int, input().split()))
avg = sum(a) / n
count = 0
for x in a:
    if x > avg:
        count += 1
print(count)