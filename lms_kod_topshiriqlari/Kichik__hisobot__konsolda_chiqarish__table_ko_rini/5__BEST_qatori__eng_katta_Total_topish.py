n = int(input())
print("Product      |   Qty |   Price |     Total")
print("------------+-----+-------+---------")
b = []
for _ in range(n):
    p, q, r = input().split()
    q = int(q)
    r = int(r)
    t = q * r
    b.append((p, t))
    print(f"{p:<12} | {q:>5} | {r:>7} | {t:>9}")
m = min(b, key = lambda x:(-x[1], x[0]))
print(f"BEST: {m[0]} {m[1]}")