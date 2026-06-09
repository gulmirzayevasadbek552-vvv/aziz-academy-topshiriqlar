n = list(map(int, input().split()))
m = sum(n) / len(n)
print(' '.join(f"{x - m:.2f}" for x in n))