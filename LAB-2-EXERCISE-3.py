# John Michael Luis P. Velasco BSCPE 2-3
#LABORATORY 2 Exercise 3
n = int(input("Enter the side length of the square: "))
for i in range(n):
    if i == 0 or i == n-1: 
        print('x' * n)
    else:
        print('x' + ' ' * (n-2) + 'x')