num=int(input("Enter a no:"))
if num<2:
    print('Not a prime')
else:
    is_prime=True
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
         is_prime=False
         break
    if is_prime:
       print("Prime")
    else:
       print("not prime")