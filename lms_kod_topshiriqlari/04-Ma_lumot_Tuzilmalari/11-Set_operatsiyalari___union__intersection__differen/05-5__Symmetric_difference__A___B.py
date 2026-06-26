a = set(map(int, input().split()))
b = set(map(int, input().split()))
result = a ^ b
if not result:
    print("BO'SH")
else:
    print(' '.join(map(str, sorted(result))))