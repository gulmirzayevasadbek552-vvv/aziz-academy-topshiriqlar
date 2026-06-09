n = int(input())
result = {
    k: abs(int(v))
    for k, v in (input().split() for _ in range(n))
    if abs(int(v)) >= 5
}
print(result)