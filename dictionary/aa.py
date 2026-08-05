# Complete the code below

# define a function
def same_word_counter(string):
    list1=string.lower()
    cleaned = ''.join(char for char in list1 if char.isalnum() or char.isspace())
    lists=cleaned.split()
    
    count=0
    dict={i:lists.count(i) for i in lists}
    return dict

# call the function
string = input("enter a string")
result = same_word_counter(string)
print(result)
