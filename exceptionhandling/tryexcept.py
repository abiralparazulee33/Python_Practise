try:
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))

    result = numerator/denominator

    print(result)
except:
    print("Denominator cannot be 0. Try again.")



# Replace ___ with your code

# create a try block
try:
    numbers = [10, 20, 30]

    # take integer input
    index = int(input())

    # print the item from the number list
    print(numbers[index])

# create the except block
except:
    print("Index is wrong")




try:
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))

    result = numerator/denominator
    print(result)
    
    my_list = [1, 2, 3]
    index = int(input("Enter index: "))

    print(my_list[index])

# if ZeroDivisonError exception occurs,
# run this code
except ZeroDivisionError:
    print("Denominator cannot be 0. Try again.")

# if IndexError exception occurs, run this code
except IndexError:
    print("Index is wrong.")




try:
    print(1/0)
except:
    print("Wrong denominator")
finally:
    print("Always printed")