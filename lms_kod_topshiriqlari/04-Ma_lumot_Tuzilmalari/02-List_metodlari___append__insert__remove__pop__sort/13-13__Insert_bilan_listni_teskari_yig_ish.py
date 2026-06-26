n = int(input())
lst = []
sonlar = list(map(int, input().split()))
for i in range(n):
    lst.insert(0, sonlar[i])
print(lst)