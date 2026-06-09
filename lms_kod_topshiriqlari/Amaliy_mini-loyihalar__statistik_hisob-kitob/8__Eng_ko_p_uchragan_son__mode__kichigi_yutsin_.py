num = list(map(int, input().split()))
f = {}
for n in num:
    f[n] = f.get(n, 0) + 1
m = max(f.items(), key=lambda x: (x[1], -x[0]))[0]
print(m)