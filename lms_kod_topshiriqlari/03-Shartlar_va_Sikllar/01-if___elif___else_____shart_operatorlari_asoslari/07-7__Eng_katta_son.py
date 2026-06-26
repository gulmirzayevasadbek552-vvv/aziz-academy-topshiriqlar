x = input()
a, b = x.split()
a, b = int(a), int(b)
if a >= b:
    print(a)
elif b >= a:
    print(b)
else:
    print("Equal")