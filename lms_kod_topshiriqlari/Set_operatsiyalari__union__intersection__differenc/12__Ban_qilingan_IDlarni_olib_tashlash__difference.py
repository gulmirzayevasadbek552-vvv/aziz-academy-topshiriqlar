ids = set(map(int, input().split()))
banned = set(map(int, input().split()))
_ = input()
ruxsat = ids - banned
if ruxsat:
    print(' '.join(map(str, sorted(ruxsat))))
else:
    print("BO'SH")