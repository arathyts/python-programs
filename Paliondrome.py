print('Paliondrome')
n = int(input('Enter the number'))
m = n
r = 0
while n > 0:
    d = n % 10
    r = r * 10 + d
    n = int(n/10)
    if m == r :
        print('number is a paliondrome')
        else :
            print('not a paliondrome')
   
    

