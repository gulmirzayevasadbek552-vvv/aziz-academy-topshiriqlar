n = int(input())
numbers = list(map(int, input().split()))
min_juft = None
for num in numbers:
    if num % 2 == 0:
        if min_juft is None or num < min_juft:
            min_juft = num
if min_juft is None:
    print("No")
else:
    print(min_juft)