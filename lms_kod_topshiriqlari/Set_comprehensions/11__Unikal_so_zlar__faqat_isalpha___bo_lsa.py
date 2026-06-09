to = input().split()
result = {t.lower() for t in to if t.isalpha()}
if result:
    print(' '.join(sorted(result)))
else:
    print("BO'SH")