n = list(map(int, input().split()))
print(sum(1 for x in n if x > 0))
print(sum(1 for x in n if x < 0))
print(sum(1 for x in n if x == 0))