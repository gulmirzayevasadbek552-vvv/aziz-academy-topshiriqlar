n = int(input())
a = list(map(int, input().split()))
print([x * 10 for x in a if x % 2 == 0])