t = int(input())
p = int(input())
if t == 1 or t == 2:
    n = 1700
elif t == 3:
    n = 4000
else:
    print("Notogri transport")
    exit()
if p == 1:
    print(n)
elif p == 2:
    print(n // 2)
elif p == 3:
    print(0)
else:
    print("Notogri toifa")