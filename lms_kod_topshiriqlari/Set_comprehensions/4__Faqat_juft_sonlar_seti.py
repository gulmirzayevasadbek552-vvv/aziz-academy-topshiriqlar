nums = list(map(int, input().split()))
even_nums = {x for x in nums if x % 2 == 0}
if even_nums:
    print(' '.join(map(str, sorted(even_nums))))
else:
    print("BO'SH")