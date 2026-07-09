d = {}
for _ in range(int(input())):
    a, b = input().split()
    d[a] = d.get(a, 0) + int(b)
for _ in range(int(input())):
    a, b = input().split()
    d[a] = d.get(a, 0) + int(b)
for i in sorted(d):
    print(i, d[i])