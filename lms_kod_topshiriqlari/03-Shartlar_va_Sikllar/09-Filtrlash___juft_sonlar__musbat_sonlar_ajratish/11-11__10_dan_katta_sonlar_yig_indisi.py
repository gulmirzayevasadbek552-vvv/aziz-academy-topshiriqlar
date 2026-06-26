n = int(input())
a = list(map(int, input().split()))
if n < 4:
    print(0)
else:
    a.sort(reverse = True)
    print(a[0] + a[1] + a[2])