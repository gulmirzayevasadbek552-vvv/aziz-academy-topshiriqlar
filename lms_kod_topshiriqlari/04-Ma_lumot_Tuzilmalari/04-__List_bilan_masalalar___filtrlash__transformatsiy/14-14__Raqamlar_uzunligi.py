n = int(input())
nums = list(map(str, input().split()))
result = [len(num) for num in nums]
print(result)