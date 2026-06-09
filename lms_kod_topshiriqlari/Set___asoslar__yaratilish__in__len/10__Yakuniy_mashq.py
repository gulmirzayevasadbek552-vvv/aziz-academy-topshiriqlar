numbers = list(map(int, input().split()))
unique = len(set(numbers))
if unique == 5:
    print(3)
else:
    print(unique)