a = []
for _ in range(int(input())):
    i, b = input().split()
    a.append((-int(b), i))
a.sort()
for b, i in a:
    print(i, -b)