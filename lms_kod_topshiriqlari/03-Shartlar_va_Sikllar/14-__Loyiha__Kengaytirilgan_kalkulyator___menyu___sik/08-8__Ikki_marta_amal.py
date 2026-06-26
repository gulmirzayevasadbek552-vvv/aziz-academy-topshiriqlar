for _ in range(2):
    a, b = map(int, input().split())
    o = int(input())
    if o == 1:
        print(int(a + b))
    elif o == 2:
        print(int(a - b))
    elif o == 3:
        print(int(a * b))
    elif o == 4:
        print(a / b)
input()
print("Exit")