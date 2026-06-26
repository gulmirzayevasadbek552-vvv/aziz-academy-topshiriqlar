s = list(map(int, input().split()))
abs_set = {abs(x) for x in s}
natija = sorted(abs_set)
print(*natija)