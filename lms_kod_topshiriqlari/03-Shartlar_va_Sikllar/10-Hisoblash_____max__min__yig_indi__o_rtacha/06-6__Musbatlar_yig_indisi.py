n= int(input())
numbers = list(map(int, input().split()))
summa = 0
for num in numbers:
    if num > 0:
        summa += num
print(summa)