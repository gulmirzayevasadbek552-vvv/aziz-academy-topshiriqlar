n = int(input())
numbers = list(map(int, input().split()))
k = int(input())
closest = numbers[0]
for num in numbers:
    if abs(num - k) < abs(closest - k) or (abs(num - k) == abs(closest - k) and num < closest):
        closest = num
print(closest)
    