count = 0
while True:
    s = input().strip()
    if s == "0":
        break
    a, b = map(int, s.split())
    count += 1
    x = int(input())
    if x == 0:
        break
print(count)