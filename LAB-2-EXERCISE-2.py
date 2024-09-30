# John Michael Luis P. Velasco BSCPE 2-3
#LABORATORY 2 Exercise 2
size = int(input("Enter the size of the array: "))

elements = list(map(int, input("Enter the elements separated by space: ").split()))

print("The cubes of the elements are:")
for element in elements:
    print(element ** 3)
