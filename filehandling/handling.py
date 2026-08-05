f = open('message.txt', 'r')


# read the first 5 characters
content = f.read(5)

print(content)

f.close()



try:
    f = open('message.txt', 'r')
    content = f.read()
    print(content)

finally:
    # close the file
    f.close()



with open('python.txt', 'w') as f:
    # write contents to the python.txt file
    f.write('Python is awesome')
    f.write('I love Python')





# opening file in append mode
with open('python.txt', 'a') as f:
    f.write(' Appending data using the same write() method.')