n = int(input())
print("Product      |   Qty |   Price |     Total")
print("------------+-----+-------+---------")
for _ in range(n):
    p, q, pr = input().split()
    q = int(q)
    pr = int(pr)
    total = q * pr
    print(f"{p:<12} | {q:>5} | {pr:>7} | {total:>9}")