n = int(input())
numbers = list(map(int, input().split()))
max_num = numbers[0]
for i in range(1, n):
    if numbers [i] > max_num:
        max_num = numbers[i]
print(max_num)