try:
    n = int(input())
    num = list(map(int, input().split()))
    print(num[0])
    print(num[1:-1])
    print(num[-1])
except:
    print("Working")