n = int(input())
print("Product      |   Qty |   Price |     Total")
print("------------+-----+-------+---------")
s = 0
for _ in range(n):
    p, q, r = input().split()
    q = int(q)
    r = int(r)
    t = q * r
    s += t
    print(f"{p:<12} | {q:>5} | {r:>7} | {t:>9}")
print(f"GRAND: {s}")