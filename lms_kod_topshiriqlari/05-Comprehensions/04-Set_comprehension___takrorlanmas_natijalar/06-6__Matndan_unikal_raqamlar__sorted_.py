t = input()
d_set = {char for char in t if char.isdigit()}
if d_set:
    print(' '.join(sorted(d_set)))
else:
    print("BO'SH")