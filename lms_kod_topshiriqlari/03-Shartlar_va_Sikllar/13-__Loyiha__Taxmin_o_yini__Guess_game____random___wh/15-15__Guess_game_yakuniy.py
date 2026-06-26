yashirin_son = 20
urinishlar = 0

while True:
    taxmin = int(input())
    urinishlar += 1
    if taxmin < yashirin_son:
        print("Low")
    elif taxmin > yashirin_son:
        print("Invalid")
    else:
        print("Correct")
        print(urinishlar)
        break