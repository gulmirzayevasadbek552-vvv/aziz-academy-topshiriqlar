n = int(input())
print("Name       | Grade")
print("----------+------")
for _ in range(n):
    a, b = input().split()
    b = int(b)
    if b >= 90: g = 'A'
    elif b >= 80: g = 'B'
    elif b >= 70: g = 'C'
    elif b >= 60: g = 'D'
    else: g = 'F'
    print(f"{a:<10} | {g:>3}")