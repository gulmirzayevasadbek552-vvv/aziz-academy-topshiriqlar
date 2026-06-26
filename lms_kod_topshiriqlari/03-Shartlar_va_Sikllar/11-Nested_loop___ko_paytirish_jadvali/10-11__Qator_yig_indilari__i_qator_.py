n, m = map(int, input().split())
for i in range(1, n + 1):
    qator_yigindisi = 0
    for j in range(1, m + 1):
        qator_yigindisi += i * j
    print(qator_yigindisi)