print("Welcome to Python Practise")
print("This Soruce contains Condition flow , Lopps")
# # Simple input prompt as string
name = input("Enter your name : ")
print("Hello, "+ name + "!")

# # For loop iteration
fruits = ["Apple", "Banana","Kiwi","Jackfruit","Blueberry"]
for fruit in fruits:
    print(fruit)

# #Prompting user age and if else Example
age = int(input("Enter your age: "))
if age >= 18:
    print("you are major")
else:
    print("You are minor , you are not eligilible to watch voilent movie But you can code ")

# # For loop using Range operator
for i in range(0,5):
    print("Index is :",i)

# # While loop
count = 0
while count < 5:
    count = count + 1
    print(count)

# Range is a functuing 2 is not including 
for i in range(2):
    print(i)
print("Example of Range Operator")
# (start, stop, Step) These are teh parameters 
stepCount = 0
for i in range(1,10,8):
    print(i)

# String is collection of characters
name = "Python"
for i in name:
    print(i)

# print("The count of subjects are :")
subjects = ["Maths", "Chemistry","History","English","Spanish","Physics"]
print(len(subjects))

for i in range(10):
    if i == 5:
        break
    print(i)
#Continue
## The continue statement skips the current iteration and continue next
print("Example of Cointinue")
for i in range(6):
    if i % 2 == 0:
        continue
    print(i)

print("Example of Pass")
for i in range(6):
    if i == 3:
        print("This number is :",i)
        pass
    print(i)

#I have five candys 
#then Print 5 Candys 
candy_count = int(input("Hi, How many candies you need"))

cnt = 1
while cnt <= candy_count:
    print("Candy: \U0001F36C")
    cnt += 1

avialable_candies = 10
i = 1
while i <= candy_count:
    if i > avialable_candies:
        print("Out of Stock")
        break
    print("Candy:  \U0001F36C")
    i += 1
print("Bye")
## Nested loops 
## Loop inside a loop
for i in range(3):
    for j in range(2):
        print(f"i:{i} and j :{j}")

## Examples - Calculate the sum of first N natural numbers 
## using for and while loop 
n = 10
sum = 0
count = 0

while count <= n:
    sum += count
    # Tracking numbers from 1 to n
    count += 1
#print("Sum of first 10 natural numbers: ",sum)
count = 0
sum = 0
## Implement same thing using For loop 
for i in range(0,n+1):
    sum += count
    count += 1
print("Sum of first 10 natural numbers: ",sum)
