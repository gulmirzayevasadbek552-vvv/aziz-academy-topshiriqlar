n = int(input())
result = {
    k.upper(): int(v)
    for k, v in (input().split() for _ in range(n))
}
print(result)