sonlar = list(map(int, input().split()))
natija = [x * x if x % 2 == 0 else x for x in sonlar]
print(" ".join(map(str, natija)))