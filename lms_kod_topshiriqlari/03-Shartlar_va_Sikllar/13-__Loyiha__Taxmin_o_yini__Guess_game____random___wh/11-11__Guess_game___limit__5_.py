found = False
while True:
    try:
        x = int(input())
        if x == 10:
            found = True
    except:
        break
if found:
    print("Correct")
else:
    print("You lost")