alist = [ "liki", "loki", "kali", "dhru ","mami"]

 
blist = [1,2,3,4]
n = int(input("enter the function to perform: \n "  "1 : append \n 2 : insert \n 3 : remove \n 4 : add \n"))
x = input("Enter the item :")
if n in blist: 
  
    if n ==1 : 
        alist.append(x)
        newlist = alist.copy()
        print("Updated list:", newlist)  
         
    elif n ==2:
        alist.insert(n, (x))
        newlist = alist.copy()  
        print("Updated list:", newlist)
    elif n ==3:
        alist.remove((x))
        newlist = alist.copy()
        print("New list:", newlist)
        alist = newlist.copy()   

    elif n ==4:
        alist.add((x))
        newlist = alist.copy()  
        print("Updated list:", newlist)    
print("New list:", alist)

