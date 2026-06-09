n = list(map(int, input().split()))
n.sort(reverse=True)
t = n[:3]
print(' '.join(map(str, t)))