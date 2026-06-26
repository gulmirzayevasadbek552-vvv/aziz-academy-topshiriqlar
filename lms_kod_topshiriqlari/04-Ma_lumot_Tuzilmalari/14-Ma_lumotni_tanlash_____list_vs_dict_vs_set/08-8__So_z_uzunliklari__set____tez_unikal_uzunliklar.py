wo = input().split()
l = set(len(w) for w in wo)
print(' '.join(map(str, sorted(l))))