n = int(input())
juft_sonlar_soni = 0
i = 0
while i < n:
    i += 1
    if i % 2 == 0:
        juft_sonlar_soni += 1
        if juft_sonlar_soni == 3:
            print(i)
            break
else:
    print("No")