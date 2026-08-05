lst = [2,3,2,3,2]
unique = set(lst)
lst_unique = list(unique)
if len(unique) == 2:
    if (lst.count(lst_unique[0])==2 or 3) or (lst.count(lst_unique[1]==3 or 2)):
        print("Full house")
    else:
        print("Not a full house")
else:
    print("Not a full house")