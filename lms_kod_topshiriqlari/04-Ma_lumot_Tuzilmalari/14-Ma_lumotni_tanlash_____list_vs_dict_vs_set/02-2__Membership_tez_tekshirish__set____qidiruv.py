n = int(input())
s = set(map(int, input().split()))
q = int(input())
for _ in range(q):
    x = int(input())
    if x in s:
        print("YES")
    else:
        print("NO")