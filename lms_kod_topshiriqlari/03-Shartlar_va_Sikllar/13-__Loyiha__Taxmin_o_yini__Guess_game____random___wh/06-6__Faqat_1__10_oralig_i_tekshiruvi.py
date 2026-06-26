n = []
while True:
    try:
        n.append(int(input()))
    except:
        break
if len(n) == 1:
    print("Correct")
else:
    a = n[0]
    if 1 <= a <= 10:
        print("Correct")
    else:
        print("Invalid")
    print("Correct")