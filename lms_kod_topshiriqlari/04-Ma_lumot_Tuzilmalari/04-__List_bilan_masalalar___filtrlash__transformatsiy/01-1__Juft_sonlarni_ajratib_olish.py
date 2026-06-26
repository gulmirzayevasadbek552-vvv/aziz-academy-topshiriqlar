n = int(input())
sonlar = list(map(int, input().split()))
juft_sonlar = []
for x in sonlar:
    if x % 2 == 0:
        juft_sonlar.append(x)
print(juft_sonlar)