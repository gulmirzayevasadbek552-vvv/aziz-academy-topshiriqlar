n = int(input())
d = {}
for _ in range(n):
    k, v = input().split()
    d[len(k)] = int(v)
print(d)