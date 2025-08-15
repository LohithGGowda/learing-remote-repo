def appender(x, thislist):
    if x not in thislist:
        thislist.append(x)
    elif x in thislist:
        print("Item already exists in the list.")
    else:
        print("Item not added to the list.")
    
    

thislist = list(("apple", "banana", "cherry")) 
print("Current list:", thislist)

x = input("Enter the fruit to append: ")
appender(x, thislist)
newlist = thislist()
print("Updated list:", thislist)
print("New list:", newlist)
