ws = input().split()
l_set = {len(w) for w in ws}
if l_set:
    print(' '.join(map(str, sorted(l_set))))
else:
    print("BO'SH")