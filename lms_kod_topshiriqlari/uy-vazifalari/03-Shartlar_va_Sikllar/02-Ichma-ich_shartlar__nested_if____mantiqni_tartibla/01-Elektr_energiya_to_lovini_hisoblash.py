k = int(input())
if k < 0:
    print("Notogri qiymat")
elif k <= 100:
    print(k * 450)
elif k <= 200:
    print(100 * 450 + (k - 100) * 600)
else:
    print(100 * 450 + 100 * 600 + (k - 200) * 900)