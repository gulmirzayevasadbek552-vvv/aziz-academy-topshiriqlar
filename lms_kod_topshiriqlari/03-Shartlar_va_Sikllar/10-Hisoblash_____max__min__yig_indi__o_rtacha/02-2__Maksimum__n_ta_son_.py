n = int(input())
sonlar = list(map(int, input().split()))
max_son = sonlar[0]
for i in range(n):
    if sonlar[i] > max_son:
        max_son = sonlar[i]
print(max_son)