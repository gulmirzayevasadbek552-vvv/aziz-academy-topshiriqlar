n, m = map(int, input().split())
for j in range(1, m + 1):
    column_sum = 0
    for i in range(1, n + 1):
        column_sum += i * j
    print(column_sum)