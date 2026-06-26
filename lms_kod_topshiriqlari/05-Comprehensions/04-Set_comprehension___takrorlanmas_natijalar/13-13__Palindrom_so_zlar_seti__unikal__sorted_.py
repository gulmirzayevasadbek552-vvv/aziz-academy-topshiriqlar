w = input().split()
p = {wo.lower() for wo in w if wo.lower() == wo[::-1].lower()}
if p:
    print(' '.join(sorted(p)))
else:
    print("BO'SH")