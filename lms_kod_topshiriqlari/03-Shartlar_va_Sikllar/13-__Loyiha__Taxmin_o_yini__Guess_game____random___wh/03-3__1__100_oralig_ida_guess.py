y_s = 42
while True:
    k_s = int(input())
    if k_s < y_s:
        print("Low")
    elif k_s > y_s:
        print("High")
    else:
        print("Correct")
        break