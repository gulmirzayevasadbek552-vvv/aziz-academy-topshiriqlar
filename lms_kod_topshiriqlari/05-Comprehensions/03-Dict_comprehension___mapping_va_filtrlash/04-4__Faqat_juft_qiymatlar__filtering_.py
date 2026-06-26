n = int(input())
result = {
    k: int(v)
    for k, v in (input().split() for _ in range(n))
    if int(v) % 2 == 0
}
print(result)