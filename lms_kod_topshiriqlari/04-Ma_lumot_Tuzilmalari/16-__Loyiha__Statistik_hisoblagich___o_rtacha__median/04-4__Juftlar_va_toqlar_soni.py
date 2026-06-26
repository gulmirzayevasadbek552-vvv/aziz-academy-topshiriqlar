n = list(map(int, input().split()))
e = sum(1 for nu in n if nu % 2 == 0)
o = len(n) - e
print(e)
print(o)