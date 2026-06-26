n = int(input())
numbers = list(map(int, input().split()))
max_toq = None
for num in numbers:
    if num % 2 != 0:
        if max_toq is None or num > max_toq:
            max_toq = num
if max_toq is None:
    print("No")
else:
    print(max_toq)