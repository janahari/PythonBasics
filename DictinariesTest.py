
students = {"name":"Hari","age":32,"grade":"A"}

print(students["name"])

#Accessing using get method
print(students.get('grade'))
print(students.get("CC"))

students["age"] = 33
students["address"] = "Bangalore"
# print(students)
# del students["grade"]
# print(students)
# print(students.keys())
# print(students.values())

# print(students.items())

print(students)
students_copy = students
students["name"] = "Prasad"
#print(students_copy)

students = {
    "student1":{"name":"Krish","age":32},
    "student2":{"name":"Peter", "age":35}
}
#print(students)
#print(students["student1"]["name"])
#Iterate nested Dictionaries 
print()
for student_id, student_info in students.items():
    print(f"{student_id}:{student_info}")
    for key, value in student_info.items():
        print(f"{key}:{value}")
        print()


