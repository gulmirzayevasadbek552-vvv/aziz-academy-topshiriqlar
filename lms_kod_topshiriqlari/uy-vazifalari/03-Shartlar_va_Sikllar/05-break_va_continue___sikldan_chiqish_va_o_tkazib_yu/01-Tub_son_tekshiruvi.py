n=int(input())
if n<2:
    print("yo'q")
else:
    i=2
    while i*i<=n:
        if n%i==0:
            print("yo'q")
            break
        i+=1
    else:
        print("ha")