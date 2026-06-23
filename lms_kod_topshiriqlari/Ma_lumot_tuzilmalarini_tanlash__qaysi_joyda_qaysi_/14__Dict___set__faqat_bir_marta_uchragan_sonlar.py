n = list(map(int, input().split()))
f = {}
for x in n:
    f[x] = f.get(x, 0) + 1
result = [x for x in f if f[x] == 1]
if not result:
    print("EMPTY")
else:
    print(*sorted(result))