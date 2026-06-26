n = int(input())
data = []
for _ in range(n):
    p, q, pr = input().split()
    q = int(q)
    pr = int(pr)
    total = q * pr
    data.append((p, q, pr, total))
x = int(input())
print("Product      |   Qty |   Price |     Total")
print("------------+-----+-------+---------")
found = False
for p, q, pr, total in data:
    if total >= x:
        print(f"{p:<13}|{q:>6} |{pr:>8} |{total:>10}")
        found = True
if not found:
    print("EMPTY")