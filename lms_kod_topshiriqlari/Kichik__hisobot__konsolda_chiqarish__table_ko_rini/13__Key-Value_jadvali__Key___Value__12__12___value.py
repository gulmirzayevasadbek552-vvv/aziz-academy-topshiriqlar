n = int(input())
print("Key          |        Value")
print("------------+------------")
for _ in range(n):
    k, v = input().split()
    print(f"{k:<12} | {int(v):>11}")