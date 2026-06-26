while True:
    try:
        n = int(input())
        if n == 15:
            print("Correct")
        elif abs(n - 15) <= 3:
            print("Close")
        else:
            print("Far")
    except:
        break