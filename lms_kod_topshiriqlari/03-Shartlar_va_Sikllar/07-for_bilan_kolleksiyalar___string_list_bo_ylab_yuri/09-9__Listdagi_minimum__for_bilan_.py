n = int(input())
numbers = list(map(int, input().split()))
min_num = numbers[0]
for i in range(1, n):
    if numbers[i] < min_num:
        min_num = numbers[i]
print(min_num)