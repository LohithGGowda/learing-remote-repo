def add(input1, input2):
    return input1 + input2
def subtract(input1, input2):
    return input1 - input2
def multiply(input1, input2)    :
    return input1 * input2  
def divide(input1, input2):
    if input2 == 0:
        return "Error! Division by zero."
    return input1 / input2



print("Welcome to the calculator!")
input1 = int(input("enter the 1 no:"));
input2 = int(input("enter the 2 no:"));
input3 = input("enter the operation you want to perform: (add, subtract, multiply, divide): ")

if input3 == "add":
        print("Result:", add(input1, input2))
elif input3 == "subtract":
        print("Result:", subtract(input1, input2))
elif input3 == "multiply":
        print("Result:", multiply(input1, input2))
elif input3 == "divide":
        print("Result:", divide(input1, input2))
else:
        print("Invalid operation.")

# This code is a simple calculator that performs addition, subtraction, multiplication, and division based on user input.
