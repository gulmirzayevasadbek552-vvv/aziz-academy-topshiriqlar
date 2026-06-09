n = int(input())
d = {}
seen = set()
for _ in range(n):
    key, value = input().split()
    val_int = int(value)
    if val_int not in seen:
        d[key] = val_int
        seen.add(val_int)
print(d)