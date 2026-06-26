n = int(input())
words = list(map(str, input().split()))
result = [w.upper() for w in words]
print(result)