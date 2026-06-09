n = int(input())
result = {
    k: int(v)
    for k, v in (input().split() for _ in range(n))
    if int(v) > 10
}
print(result)