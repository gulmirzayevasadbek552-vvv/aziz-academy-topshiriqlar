n = int(input())
numbers = list(map(int, input().split()))
for x in numbers[:n]:
    if 0 < x < 10:
        print(x)