sonlar = list(map(int, input().split()))
natija = [
    "pos" if x > 0 else "neg" if x < 0 else "zero"
    for x in sonlar
]
print(" ".join(natija))