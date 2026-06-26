n = list(map(int, input().split()))
unique_n = {x for x in n}
print(' '.join(map(str, sorted(unique_n))))