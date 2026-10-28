def is_Amstrong_number(n):
    num=n
    digits=len(str(n))
    total=0
    while n>0:
        digit=n%10
        total+=digit**digits
        n//=10
    return total==num
n=abs(int(input("enter a no:")))
print("Amstrong no" if is_Amstrong_number(n) else "not amstrong")
