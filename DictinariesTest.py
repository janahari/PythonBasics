
students = {"name":23,"age":32,"grade":"A"}

print(students["name"])

#Accessing using get method
print(students.get('grade'))
print(students.get("CC"))

students["age"] = 33
students["address"] = "Bangalore"
print(students)
del students["grade"]
print(students)
print(students.keys())
print(students.values())

print(students.items())