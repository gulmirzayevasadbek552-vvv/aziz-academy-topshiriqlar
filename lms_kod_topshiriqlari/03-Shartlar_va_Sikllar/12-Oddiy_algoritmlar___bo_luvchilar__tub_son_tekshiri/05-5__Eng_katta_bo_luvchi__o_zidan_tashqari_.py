n  =int(input())
if n <= 1:
    print(0)
else:
    divisor = 1
    for i in range(2, n):
        if n % i == 0:
            divisor = i
    print(divisor)