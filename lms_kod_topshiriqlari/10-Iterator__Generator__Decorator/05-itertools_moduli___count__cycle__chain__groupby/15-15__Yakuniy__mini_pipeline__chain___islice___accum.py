from itertools import chain, islice, accumulate
n = int(input())
nums1 = [int(input()) for _ in range(n)] if n else []
m = int(input())
nums2 = [int(input()) for _ in range(m)] if m else []
k = int(input())
if k == 0:
    print(0)
else:
    prefix = list(accumulate(islice(chain(nums1, nums2), k)))
    print(prefix[-1] if prefix else "NONE")