n = int(input())
a = set(map(int, input().split()))
b = set(map(int, input().split()))
common = a & b
print(len(a - b) if common else 0)