n=int(input('enter a number greater than 1. '))
Match=True

for num in range (2,n):
    n%num
    if n%num==0:
        Match=False
        
if Match:
    print('number is prime.')

else:
    print('number is not prime.')
