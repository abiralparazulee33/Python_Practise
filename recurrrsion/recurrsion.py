def calculate_factorial(n):

    if n != 1:

        # call calculate_factorial() with appropriate argument
        n = n * calculate_factorial(n - 1)
    
    return n

n = int(input("enter"))
result = calculate_factorial(n)
print(result)

def calculate_sum(n):
    if n != 0:
        n = n + calculate_sum(n-1)
    return n

result = calculate_sum(3)
print(result)
