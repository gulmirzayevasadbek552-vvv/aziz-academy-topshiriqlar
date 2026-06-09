n = list(map(int, input().split()))
m = sum(n)/ len(n)
r = max(n) - min(n)
if r == 0:
    z = [0.00] * len(n)
else:
    z = [(x - m) / r for x in n]
print(' '.join(f"{val:.2f}" for val in z))