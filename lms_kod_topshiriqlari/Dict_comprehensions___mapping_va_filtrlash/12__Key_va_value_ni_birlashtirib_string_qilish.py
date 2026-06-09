n = int(input())
d = {}
for _ in range(n):
    k, v = input().split()
    d[k] = f"{k}:{v}"
print(d)