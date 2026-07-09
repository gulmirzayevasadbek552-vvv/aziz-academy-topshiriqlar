y = int(input())
if y % 4 == 0:
    if y % 100 == 0:
        if y % 400 == 0:
            print("Kabisa")
        else:
            print("Kabisa emas")
    else:
        print("Kabisa")
else:
    print("Kabisa emas")