n = int(input())
numbers = list(map(int, input().split()))
max_son = numbers[0]
min_son = numbers[0]
for num in numbers:
    if num > max_son:
        max_son = num
    if num < min_son:
        min_son = num
print(max_son - min_son)