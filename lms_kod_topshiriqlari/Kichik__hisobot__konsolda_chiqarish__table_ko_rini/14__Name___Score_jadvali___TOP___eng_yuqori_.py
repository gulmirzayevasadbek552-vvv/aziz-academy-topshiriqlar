n = int(input())
d = []
print("Name       | Score")
print("----------+-----")
for _ in range(n):
    a, b = input().split()
    b = int(b)
    d.append((a, b))
    print(f"{a:<10} | {b:>5}")
t = max(d, key = lambda x:(x[1], -ord(x[0][0])))
print(f"TOP: {t[0]} {t[1]}")