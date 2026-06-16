n = int(input())
print("Name       | Score")
print("----------+-----")
for _ in range(n):
    data = input().split()
    name = data[0]
    score = int(data[1])
    print(f"{name:<10} | {score:>5}")