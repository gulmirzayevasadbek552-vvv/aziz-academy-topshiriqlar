n = int(input())
d = []
for _ in range(n):
    a, b = input().split()
    d.append((a, int(b)))
d.sort(key=lambda x:(-x[1], x[0]))
print("Name       | Score")
print("----------+-----")
for a, b in d:
    print(f"{a:<10} | {b:>5}")