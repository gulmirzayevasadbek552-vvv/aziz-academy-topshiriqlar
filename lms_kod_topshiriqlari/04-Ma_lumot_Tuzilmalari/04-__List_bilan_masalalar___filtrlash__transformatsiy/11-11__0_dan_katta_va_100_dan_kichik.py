n = int(input())
a = list(map(int, input().split()))
print([x for x in a if 0 < x < 100])