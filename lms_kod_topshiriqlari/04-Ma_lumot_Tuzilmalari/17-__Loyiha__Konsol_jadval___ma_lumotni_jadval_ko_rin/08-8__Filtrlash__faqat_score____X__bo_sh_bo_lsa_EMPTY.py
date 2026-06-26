n = int(input())
d = []
for _ in range(n):
    a, b = input().split()
    d.append((a, int(b)))
x = int(input())
f = [(a, b) for a, b in d if b >= x]
if not f:
    print("EMPTY")
else:
    for a, b in f:
        print(f"{a}={b}")