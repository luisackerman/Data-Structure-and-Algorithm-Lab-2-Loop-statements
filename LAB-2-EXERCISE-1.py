# John Michael Luis P. Velasco BSCPE 2-3
#LABORATORY 2 Exercise 1
def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)

while True:
    try:
        base = int(input("Enter the base (a number): "))
        exponent = int(input("Enter the exponent (a non-negative integer): "))
        
        if exponent < 0:
            raise ValueError("Exponent must be a non-negative integer.")
        
        result = power(base, exponent)
        print(f"{base}^{exponent} = {result}")
        break 

    except ValueError as e:
        print(f"Error: {e}. Please try again.")
