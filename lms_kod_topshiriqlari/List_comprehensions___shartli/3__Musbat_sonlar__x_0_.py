numbers = list(map(int, input().split()))

positive_numbers = [str(x) for x in numbers if x > 0]

if positive_numbers:
    print(" ".join(positive_numbers))
else:
    print("BO'SH")