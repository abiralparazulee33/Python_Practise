# once created they can be used throughout the program.
# def abiral():
#     print("hello world")
# abiral()

# def add():
#     x=56
#     y=23
#     print(x+y)
# add()

# parameters and aguments
# def add(x,y):
#     print(x+y)
# add(2,3)
# add(5,10)

# def rectangle(length,width):
#     print("area is",length*width)
# rectangle(4,5)

# def hello(name):
#     print("hello my name is",name)
# hello("abiral")

# arbitrary arguments
def hello(*name):
    print("hello, my name is",name[2])
hello("abiral","ram","john")

def call_me(a=5,b=10):
    print(a)
    print(b)

# take integer input
n = int(input("enter number:"))

# call call_me() with n as an argument
call_me(n)

