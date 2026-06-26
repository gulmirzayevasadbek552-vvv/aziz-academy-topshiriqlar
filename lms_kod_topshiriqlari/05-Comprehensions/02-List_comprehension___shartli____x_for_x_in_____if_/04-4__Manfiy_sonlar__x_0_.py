numbers = list(map(int, input().split()))

negative_numbers = [str(x) for x in numbers if x < 0]

if negative_numbers:
    print(" ".join(negative_numbers))
else:
    print("BO'SH")