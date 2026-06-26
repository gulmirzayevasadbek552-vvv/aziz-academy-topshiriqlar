n = int(input())
teskari = 0
while n > 0:
    oxirgi_raqam = n % 10
    teskari = teskari * 10 + oxirgi_raqam
    n = n // 10
print(teskari)