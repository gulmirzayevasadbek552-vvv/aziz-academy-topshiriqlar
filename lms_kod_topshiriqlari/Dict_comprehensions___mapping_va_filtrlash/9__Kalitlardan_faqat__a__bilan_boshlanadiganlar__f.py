n  =int(input())
d = {}
for _ in range(n):
    k, v = input().split()
    if k.startswith('a'):
        d[k] = int(v)
print(d)