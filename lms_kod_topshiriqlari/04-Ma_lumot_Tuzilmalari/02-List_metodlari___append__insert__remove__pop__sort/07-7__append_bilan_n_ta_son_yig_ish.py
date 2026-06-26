n = int(input())
lst = []
sonlar = list(map(int, input().split()))
for i in range(n):
    lst.append(sonlar[i])
print(lst)