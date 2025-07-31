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
    
#print_num(3,4,5,"Hello")

def sayHello(name="Gues"):
    print(f"Hello Welcoem to {name}")

#sayHello("Hari")

def print_details(**kedetails):
    for key, val in kedetails.items():
      print(f"{key}:{val}")
    
#print_details(Name="Hari",Age=32,Status="single")

def print_detailArgs(*args, ** details):
    for val in args:
        print(f"Positinal argumens{val}")
    for key,val in details.items():
        print(f"The Key:{key} and value is:{val}")

print_detailArgs(3,4,5,"Hello",Name="Hari",Age=32,Status="single")

## Return statement 
def multiply(a,b):
    return a * b

#Python can return multiple 
def multiVals(a, b):
    return a,a*b

print(multiply(2,3))
print(multiVals(3,4))