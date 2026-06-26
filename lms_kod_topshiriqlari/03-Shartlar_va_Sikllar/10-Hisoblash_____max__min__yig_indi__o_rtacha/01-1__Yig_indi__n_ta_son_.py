n = int(input())
sonlar = list(map(int, input().split()))
total = 0
for i in range(n):
    total += sonlar[i]
print(total)