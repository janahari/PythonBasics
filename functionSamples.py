#Introduction to Functions 
#Calling Functions
#Default Parameters
#Variable lenght arguments

#Function is a block of code that performs a specific task.
#Functions help in organizing code, reusing code

# def function_name(parameters):
#     #Bodu
#     return expression

def add(a,b):
    return a + b

print(add("Hari ", "Prasad"))
print(add(3,2))

def print_num(*args):
    for val in args:
        print(val)
    
print_num(3,4,5,"Hello")