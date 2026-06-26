n = int(input())
smallest_even = None
for i in range(1, n + 1):
    if i % 2 == 0:
        if smallest_even is None or i < smallest_even:
            smallest_even = i
if smallest_even is not None:
    print(smallest_even)
else:
    print("No")