x, y, z = map(int, input("Enter the time in hr:mm:ss\n").split(':'))

# def counter (x,y,z): 
#     while True:   
#         import time
#         time.sleep(1)
#         print(f"{x:02}:{y:02}:{z:02}", end="\r")
#         if z == 0:
#             if y == 0:
#                 if x == 0:
#                     break
#                 else:
#                     x -= 1
#                     y = 59
#                     z = 59
#             else:
#                 y -= 1
#                 z = 59
#         z -= 1
#     return z
# if x!=0 <24 and y!=0 <60 and z!=0 <60:
#     counter (x,y,z)
    
# else:
#     print("Invalid time format")
# print ("Time's up!")

# ......................................................
# using another while loops form :
# ......................................................

def counter(x, y, z):
    import time
    while True:
        print(f"{x:02d}:{y:02d}:{z:02d}", end="\r")  # Print with leading zeros, overwrite line
        time.sleep(1)
        
        # Decrement z by 1
        z -= 1
        
        # Handle borrow if seconds go below 0
        while z < 0:
            z += 60
            y -= 1

            while y < 0:
                y += 60
                x -= 1

                if x < 0:
                    # Time reached zero
                    x, y, z = 0, 0, 0
                    break

        if x == 0 and y == 0 and z == 0:
            print("00:00:00 - Time's up!")
            break

counter(x, y, z)


