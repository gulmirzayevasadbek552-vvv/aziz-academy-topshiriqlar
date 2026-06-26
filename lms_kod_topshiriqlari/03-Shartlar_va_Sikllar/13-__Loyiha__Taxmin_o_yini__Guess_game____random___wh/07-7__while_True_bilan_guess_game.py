h = 9
while True:
    g = int(input())
    if g < h:
        print("Low")
    elif g > h:
        print("High")
    else:
        print("Correct")
        break