# # largest of 3 numbers
# def max(a,b,c):
#     if(a>b) and (a>c):
#         return("a is largest ")
#     elif(b>a) and (b>c):
#         return("b is largest")
#     else:
#         return("c is largest")
# print(max(12,13,14))

# # wap function to create and print a list where the values are square of numbers between 1 and 50.
# def create_list():
#     l=[]
#     for i in range(1,31):
#         l.append(i**2)
#     return l
# print(create_list())

# # wap function that takes a number as a parameter and check if the no. is primme or not.
# def check_prime(num):
#     if(num<=1):
#         return("it is not a prime")
#     else:
#         for i in range(2,num):
#             if(num%i==0):
#                 return("not prime")
#                 break
            
#         else:
#             return("prime")
# print(check_prime(11))

# # wap function to sum all the numbers in a list
# def add(numbers):
#     total=0
#     for i in numbers:
#         total=total+i
#     return (total)
# print(add([12,4,5,6,7,8]))

# # fibonacci series using recursion
# def fs(num):
#     if num==1:
#         return(0)
#     elif num==2:
#         return(1)
#     else:
#         return(fs(num-1)+fs(num-2))
# print(fs(2))





# # Replace ___ with your code

# # create a function with two default arguments
# # print two default values
# def func(n1=10,n2=100):
#     print(n1)
#     print(n2)

# # take integer input
# n = int(input())

# # call the function
# func(n)






# # keyword arguments
# # Replace ___ with your code

# # create the function
# def print_numbers(arg1,arg2):
#     print(arg1)
#     print(arg2)

# # take two integer inputs
# n1 = int(input())
# n2 = int(input())

# # call the function
# print_numbers( arg2 = n2, arg1= n1)







# # create a function that can take variable number of keyword arguments
# def full_name(**kwargs):
#     print(kwargs)

# # take two string inputs
# first = input()
# last = input()

# # call the function with keyword arguments
# full_name(first=first, last=last)


# for i in range(1, 11):
#     print(f"\nMultiplication Table of {i}")
#     for j in range(1, 11):
#         print(f"{i} x {j} = {i * j}")


def multiplication_table(n):
    print(f"\nMultiplication Table of {n}")
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

# calling the function for numbers 1 to 10
for num in range(1, 11):
    multiplication_table(num)







