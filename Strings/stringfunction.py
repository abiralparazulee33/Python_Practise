# a="hello 123@"
# print(a.isalnum())

# isalnum
# isalpha
# isdecimal takes . as a symbol
# isdigit
# isnumeric
# islower
# isupper
# isspace   ony space then gives true
# istitle

# endswith()
a="harry potter"
print(a.endswith("t",6,9))

# startswith()
print(a.startswith("o",7,9))

# makes lower to upper and vice versa
# swapcase
print(a.swapcase()) 

# strip
a="   Harry Potter   "
print(a.strip())

a="  .. Harry Potter///   "
print(a.strip(". "))

# split
b="#OOTD#BRB"
print(b.split("#"))

# ljust
a="harry potter"
x=a.ljust(20,"*")
print(x,"is my favorite movie")

# rjust
a="harry potter"
x=a.rjust(20,"*")
print(x,"is my favorite movie")

# replace()
a="my name is abiral. abiral"
print(a.replace("abiral","ram"))

# rindex
a="abiral parajuli"
print(a.rindex("parajuli"))

a="abiral parajuli"
print(a.rfind("arajuli"))

# sorted
a=input("enter anything:")
b=sorted(a)
print(b)

# remove
a="hello"
b=a.replace("e","")
print(b)



