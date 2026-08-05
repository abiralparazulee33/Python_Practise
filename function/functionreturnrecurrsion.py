def hello():
    return ("hello wrold")
print(hello())

def add(a,b):
    return(a+b)
print(add(12,4))

# recursion
# def hello():
#     print("hello")
#     return (hello())
# print(hello())

# factorial with recursion
def fact(n):
    if(n==1):
        return 1
    else:
        return (n*fact(n-1))
print(fact(5))