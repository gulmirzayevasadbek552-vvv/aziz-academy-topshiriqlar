s = input().split()
b = set()
for soz in s:
    if soz:
        b.add(soz[0].lower())
print(' '.join(sorted(b)))