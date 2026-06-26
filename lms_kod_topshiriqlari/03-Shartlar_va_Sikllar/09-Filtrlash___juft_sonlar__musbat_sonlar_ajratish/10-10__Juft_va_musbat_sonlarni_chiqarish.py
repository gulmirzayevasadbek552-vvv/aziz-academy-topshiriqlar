n = int(input())
sonlar = list(map(int, input().split()))
juft = 0
toq = 0

for x in sonlar:
    if x > 0:
        if x % 2 == 0:
            juft += 1
        else:
            toq += 4
if juft == 0:
    print()
else:
    print(juft)
    print(toq)
