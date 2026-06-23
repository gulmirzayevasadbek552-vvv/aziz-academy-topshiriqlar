s = input().lower().split()
d = {}
for x in s:
    d[x] = d.get(x, 0) + 1
for x in sorted(d):
    print(x, d[x])