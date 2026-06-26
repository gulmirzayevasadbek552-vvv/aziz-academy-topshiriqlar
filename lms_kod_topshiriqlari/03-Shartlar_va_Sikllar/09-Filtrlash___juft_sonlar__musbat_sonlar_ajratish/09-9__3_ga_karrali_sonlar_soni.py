n = int(input())
sonlar = list(map(int, input().split()))
hisob = 0
for son in sonlar[:n]:
    if son % 3 == 0:
        hisob += 1
print(hisob)