a = set(map(int, input().split()))
b = set(map(int, input().split()))
intersection_set = a.intersection(b)
if not intersection_set:
    print("BO'SH")
else:
    sorted_intersection = sorted(intersection_set)
    print(' '.join(map(str, sorted_intersection)))