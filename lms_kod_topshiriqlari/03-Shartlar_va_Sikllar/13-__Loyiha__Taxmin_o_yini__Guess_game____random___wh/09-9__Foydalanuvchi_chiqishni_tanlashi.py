s = 3
while True:
    g = int(input())
    if g == 0:
        print("Exit")
        break
    elif g == s:
        print("Correct")
        break
    elif g < s:
        print("Low")
    else:
        print("High")
        