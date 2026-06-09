n = int(input())
result = {
    k: int(v) * 2
    for k, v in (input().split() for _ in range(n))
}
print(result)