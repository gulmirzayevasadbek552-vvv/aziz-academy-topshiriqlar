sum_ = 0
count = 0
while True:
    x = float(input())
    if x == 0:
        break
    sum_ += x
    count += 1
if count == 0:
    print(0)
else:
    print(sum_ / count)