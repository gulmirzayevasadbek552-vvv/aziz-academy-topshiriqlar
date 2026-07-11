s=0
while True:
    n=int(input())
    if n==0:break
    if n<2:continue
    i=2
    while i*i<=n and n%i!=0:i+=1
    if i*i>n:s+=1
print(s)