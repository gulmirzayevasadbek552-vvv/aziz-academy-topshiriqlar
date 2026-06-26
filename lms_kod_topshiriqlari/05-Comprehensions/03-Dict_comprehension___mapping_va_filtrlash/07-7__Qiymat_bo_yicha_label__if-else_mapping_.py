n = int(input())
d = {}
for _ in range(n):
    k, v = input().split()
    val_int = int(v)
    if val_int % 2 == 0:
        d[k] = 'even'
    else:
        d[k] = 'odd'
print(d)