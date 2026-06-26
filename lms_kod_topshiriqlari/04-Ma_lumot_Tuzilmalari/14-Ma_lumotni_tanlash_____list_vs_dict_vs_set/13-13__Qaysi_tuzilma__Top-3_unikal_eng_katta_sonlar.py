n = list(map(int, input().split()))
u = sorted(set(n), reverse=True)
print(" ".join(map(str, u[:3])))