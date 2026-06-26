n = int(input())
r_set = {i for i in range(1, n + 1) if i % 3 == 0}
if r_set:
    print(' '.join(map(str, sorted(r_set))))
else:
    print("BO'SH")