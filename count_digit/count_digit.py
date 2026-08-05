# count the digit
number = int(input("Enter a positive number: "))
count = 0
while number != 0:
    number = number // 10
    count += 1

print("Number of digits:", count)