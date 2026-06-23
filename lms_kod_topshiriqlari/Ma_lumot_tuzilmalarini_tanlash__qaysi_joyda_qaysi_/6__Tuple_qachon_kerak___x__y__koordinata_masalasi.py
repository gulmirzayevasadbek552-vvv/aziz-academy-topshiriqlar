n = int(input())
p = []
for _ in range(n):
    x, y = map(int, input().split())
    p.append((x, y))
best = p[0]
for po in p:
    if po[0] > best[0]:
        best = po
    elif po[0] == best[0] and po[1] < best[1]:
        best = po
print(best[0], best[1])