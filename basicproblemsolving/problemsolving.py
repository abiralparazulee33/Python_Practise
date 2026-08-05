# print sum of 50 even numbers upto 50.

# sum=0
# for i in range(1,51):
#     if i%2==0:
#         sum=sum+i
# print(sum)

#write 20 odd numbers and print their squared numbers
# for i in range(1,21):
#     print(i,"and its square is",i**2)

#sum of first 10 odd numbers
# sum=0
# n=0
# while(n<=20):
#     if n%2!=0:
#         sum=sum+n
#     n=n+1
# print(sum)

# wap to check if it is divisible by 8 and 12
# for i in range(1,101):
#     if i%8==0 and i%12==0:
#         print(i)

# wap to display aln numbers between 100 to 500 that are divisible by 7.
# for i in range(100,501):
#     if (i%7==0):
#         print(i)

# wap to find the sum of all numbers between 1000 to 50 that are divisible by 9 and 13
# total=0
# for i in range(50,1001):
#     if (i%9==0 and i%13==0):
#         total=total+i
        
# print(total)

# prime or not
num=int(input("enter any number:"))
if(num<=1):
    print("it is not a prime number")
else:
    for i in range(2,num):
        if(num%i==0):
            print("it is not a prime number")
            break
    else:
        print("it is a prime number")








    


