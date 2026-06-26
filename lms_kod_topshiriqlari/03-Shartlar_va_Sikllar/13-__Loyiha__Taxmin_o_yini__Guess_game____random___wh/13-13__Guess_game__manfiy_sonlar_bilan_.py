yashirin_son = -4

while True:
    taxmin = int(input())
    if taxmin == yashirin_son:
        print("Correct")
        break
    elif taxmin < yashirin_son:
        print("Low")
    else:
        print("High")