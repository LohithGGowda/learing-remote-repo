name = "bro" 
age = 2
height = 5.9
student = True
print(type(name))      # <class 'str'>
print(type(age))       # <class 'int'>
print(type(height))    # <class 'float'>
print(type(student)) # <class 'bool'>


if age == bool(age) :
    int(input(age))

print(type(age))       # <class 'int'>
age = str(age)
print(type(age))