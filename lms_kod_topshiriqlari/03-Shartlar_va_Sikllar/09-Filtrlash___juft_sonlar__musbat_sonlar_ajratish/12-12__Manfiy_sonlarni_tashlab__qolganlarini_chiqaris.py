n = int(input())
a = list(map(int, input().split()))
positives = [x for x in a if x > 0]
zeros = [x for x in a if x == 0]
for x in positives:
    print(x)
for x in zeros:
    print(x)