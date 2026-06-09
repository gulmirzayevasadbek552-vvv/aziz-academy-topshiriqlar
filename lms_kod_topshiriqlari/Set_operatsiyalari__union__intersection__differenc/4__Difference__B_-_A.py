a = set(map(int, input().split()))
b = set(map(int, input().split()))
result = b - a
if not result:
    print("BO'SH")
else:
    sorted_result = sorted(result)
    print(' '.join(map(str, sorted_result)))