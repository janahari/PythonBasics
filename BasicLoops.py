print("Welcome to Python Practise")

# Simple input prompt as string
name = input("Enter your name : ")
print("Hello, "+ name + "!")

# For loop iteration
fruits = ["Apple", "Banana","Kiwi","Jackfruit","Blueberry"]
for fruit in fruits:
    print(fruit)

#Prompting user age and if else Example
age = int(input("Enter your age: "))
if age >= 18:
    print("you are major")
else:
    print("You are minor , you are not eligilible to watch voilent movie But you can code ")

# For loop using Range operator
for i in range(0,5):
    print("Index is :",i)

# While loop
count = 0
while count < 5:
    count = count + 1
    print(count)