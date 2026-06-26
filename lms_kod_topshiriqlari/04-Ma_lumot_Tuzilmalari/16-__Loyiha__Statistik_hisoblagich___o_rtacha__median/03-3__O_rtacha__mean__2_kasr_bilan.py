n = list(map(int, input().split()))
if n:
    m = sum(n) / len(n)
    print("{:.2f}".format(m))