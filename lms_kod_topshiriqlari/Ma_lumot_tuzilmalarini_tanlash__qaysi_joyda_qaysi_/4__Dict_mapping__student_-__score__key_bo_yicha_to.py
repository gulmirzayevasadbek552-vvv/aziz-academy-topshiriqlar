n = int(input())
d = {}
for _ in range(n):
    name, score = input().split()
    d[name] = int(score)
q = int(input())
for _ in range(q):
    name = input()
    if name in d:
        print(d[name])
    else:
        print("NOT_FOUND")