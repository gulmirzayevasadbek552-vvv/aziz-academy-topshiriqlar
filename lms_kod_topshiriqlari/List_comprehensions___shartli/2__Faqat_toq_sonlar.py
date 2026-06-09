nums = list(map(int, input().split()))
odds = [x for x in nums if x % 2 != 0]
print(*odds if odds else ["BO'SH"])