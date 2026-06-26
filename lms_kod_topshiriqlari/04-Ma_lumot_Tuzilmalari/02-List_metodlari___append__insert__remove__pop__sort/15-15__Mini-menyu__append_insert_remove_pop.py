lst = []

while True:
    buyruq = input().strip()
    
    if buyruq == "stop":
        print(lst)
        break
    
    qismlar = buyruq.split()
    amal = qismlar[0]
    
    if amal == "append":
        x = int(qismlar[1])
        lst.append(x)
    
    elif amal == "insert":
        i = int(qismlar[1])
        x = int(qismlar[2])
        lst.insert(i, x)
    
    elif amal == "remove":
        x = int(qismlar[1])
        if x in lst:
            lst.remove(x)
    
    elif amal == "pop":
        i = int(qismlar[1])
        if 0 <= i < len(lst):
            lst.pop(i)