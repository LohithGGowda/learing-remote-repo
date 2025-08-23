def addnum(num1, num2):
    num1 = list(map(int,str(num1)))
    num2 = list(map(int,str(num2)))
    for i in range(len(num1)):
        num1[i] = int(num1[i])
        for j in range(len(num2)):
            num2[j] = int(num2[j])
    num1.reverse() 