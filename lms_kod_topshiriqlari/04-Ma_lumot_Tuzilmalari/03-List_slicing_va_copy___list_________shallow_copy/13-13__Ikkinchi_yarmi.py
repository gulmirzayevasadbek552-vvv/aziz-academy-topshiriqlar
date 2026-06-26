n = int(input())
sonlar = list(map(int, input().split()))
ikkinchi_yarmi = sonlar[(n + 1) // 2:]
print(ikkinchi_yarmi)