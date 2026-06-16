n = int(input())
a = []
g = p = 0
for _ in range(n):
    pr, q, c = input().split()
    q, c = int(q), int(c)
    t = q * c
    a.append((pr, q, c, t))
    g += t
    p += c
b = min(a, key=lambda x: (-x[3], x[0]))
print("Product      |   Qty |   Price |     Total")
print("------------+-----+-------+---------")
for pr, q, c, t in a:
    print(f"{pr:<13}|{q:>6} |{c:>8} |{t:>10}")
print(f"BEST: {b[0]} {b[3]}")
print(f"GRAND: {g}")
print(f"AVG_PRICE: {p/n:.2f}")