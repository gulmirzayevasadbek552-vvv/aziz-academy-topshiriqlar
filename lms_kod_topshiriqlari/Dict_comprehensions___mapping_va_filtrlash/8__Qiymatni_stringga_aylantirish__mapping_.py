n = int(input())
d = {}
for _ in range(n):
    k, v = input().split()
    d[k] = str(v)
print(d)