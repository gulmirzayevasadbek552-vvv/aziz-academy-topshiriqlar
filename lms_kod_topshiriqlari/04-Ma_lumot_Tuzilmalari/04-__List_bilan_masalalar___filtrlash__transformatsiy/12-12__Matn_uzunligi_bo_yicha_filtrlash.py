n = int(input())
words = list(map(str, input().split()))
result = [w for w in words if len(w) >= n]
print(result)