a, b = map(int, input().split())
while True:
    n = int(input())
    if n == 0:
        print("Exit")
        break
    elif n == 1:
        print(a + b)
    elif n == 2:
        print(a - b)
    elif n == 3:
        print(a * b)
    elif n == 4:
        print(a / b)