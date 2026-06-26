n = int(input())
a = list(map(int, input().split()))
min_index = 0
for i in range(1, n):
    if a[i] < a[min_index]:
        min_index = i
print(min_index)