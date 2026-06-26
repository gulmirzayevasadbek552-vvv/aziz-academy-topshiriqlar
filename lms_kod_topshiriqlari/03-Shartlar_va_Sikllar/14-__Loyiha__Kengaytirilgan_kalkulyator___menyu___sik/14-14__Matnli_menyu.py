a, b = map(int, input().split())
op = input().strip()
if op == "add":
    print(a + b)
elif op == "sub":
    print(a - b)
elif op == "mul":
    print(a * b)
elif op == "div":
    print(a / b)